from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from contextlib import asynccontextmanager
import warnings

warnings.filterwarnings("ignore")

# Define absolute paths
SPINE_PATH = r"C:\Users\SANAD\makemore\models\spine"
BRAIN_PATH = r"C:\Users\SANAD\Downloads\models\new_Brain"
JUDGE_PATH = r"C:\Users\SANAD\makemore\models\judge.pt"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class JudgeNN(nn.Module):
    def __init__(self):
        super(JudgeNN, self).__init__()
        # Inferred from state_dict keys: network.0, network.3, network.5
        self.network = nn.Sequential(
            nn.Linear(4, 16),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 1)
        )
        
    def forward(self, x):
        return self.network(x)

# Global model variables
models = {}

# We use lifespan to load models at startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up IntelliGuard API...")
    print(f"Using device: {device}")
    
    # Load SPINE
    try:
        print("Loading SPINE model (DistilBERT)...")
        models["spine_tokenizer"] = DistilBertTokenizer.from_pretrained(SPINE_PATH)
        models["spine_model"] = DistilBertForSequenceClassification.from_pretrained(SPINE_PATH).to(device)
        models["spine_model"].eval()
    except Exception as e:
        print(f"Warning: Failed to load SPINE model: {e}")
        
    # Load BRAIN
    try:
        print("Loading BRAIN model (XLM-RoBERTa)...")
        models["brain_tokenizer"] = AutoTokenizer.from_pretrained(BRAIN_PATH)
        models["brain_model"] = AutoModelForSequenceClassification.from_pretrained(BRAIN_PATH).to(device)
        models["brain_model"].eval()
    except Exception as e:
        print(f"Warning: Failed to load BRAIN model: {e}")
        
    # Load JUDGE
    try:
        print("Loading JUDGE model (PyTorch NN)...")
        models["judge_model"] = JudgeNN().to(device)
        state_dict = torch.load(JUDGE_PATH, map_location=device)
        models["judge_model"].load_state_dict(state_dict)
        models["judge_model"].eval()
    except Exception as e:
        print(f"Warning: Failed to load JUDGE model: {e}")
        
    print("Startup sequence complete.")
    yield
    print("Shutting down IntelliGuard API...")
    models.clear()

app = FastAPI(lifespan=lifespan, title="IntelliGuard API")

class Query(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "IntelliGuard API is running. Use POST /scan to scan text."}

@app.post("/scan")
def scan(query: Query):
    # Check if models are loaded
    if "spine_model" not in models or "brain_model" not in models or "judge_model" not in models:
        raise HTTPException(status_code=503, detail="Models are not fully loaded yet.")
        
    text = query.text
    
    # ── WHITELIST: Common safe phrases — never block these ──
    safe_phrases = ["hi", "hello", "thanks", "thank you", "ok", "okay", 
                    "yes", "no", "help", "good morning", "good evening",
                    "good night", "bye", "goodbye", "please", "sure",
                    "hey", "howdy", "welcome", "cheers", "noted"]
    if text.strip().lower() in safe_phrases:
        return {
            "verdict": "SAFE",
            "score": 0.0,
            "triggered_at": "WHITELIST",
            "reason": "Common safe phrase",
            "severity": "NONE",
            "details": {"spine_score": 0.0, "brain_score": 0.0}
        }
    
    # ── WHITELIST: Short messages (<20 chars) — skip scanning ──
    if len(text.strip()) < 20:
        return {
            "verdict": "SAFE",
            "score": 0.0,
            "triggered_at": "WHITELIST",
            "reason": "Message too short to be an injection attack",
            "severity": "NONE",
            "details": {"spine_score": 0.0, "brain_score": 0.0}
        }
    
    # 1. Run through SPINE
    spine_inputs = models["spine_tokenizer"](text, return_tensors="pt", truncation=True, padding=True).to(device)
    with torch.no_grad():
        spine_outputs = models["spine_model"](**spine_inputs)
        spine_logits = spine_outputs.logits
        # Get probabilities for the 2 classes
        spine_probs = F.softmax(spine_logits, dim=-1)
        
    # 2. Run through BRAIN
    brain_inputs = models["brain_tokenizer"](text, return_tensors="pt", truncation=True, padding=True).to(device)
    with torch.no_grad():
        brain_outputs = models["brain_model"](**brain_inputs)
        brain_logits = brain_outputs.logits
        # Get probabilities for the 2 classes
        brain_probs = F.softmax(brain_logits, dim=-1)
        
    # 3. Run through JUDGE
    # Concatenate the 2 probabilities from SPINE and 2 from BRAIN to create 4 inputs
    judge_inputs = torch.cat([spine_probs, brain_probs], dim=-1)
    
    with torch.no_grad():
        judge_output = models["judge_model"](judge_inputs)
        
        # Determine the final score and verdict
        if len(judge_output.shape) == 2 and judge_output.shape[-1] == 2:
            # If the judge outputs 2 logits
            score = F.softmax(judge_output, dim=-1)[0, 1].item()
        else:
            # If the judge outputs a single value (e.g. from 1 output node)
            score = judge_output.item()
            # If it's a raw logit (could be negative or > 1), pass it through sigmoid
            if score < 0 or score > 1:
                score = torch.sigmoid(torch.tensor(score)).item()
                
        # The judge model outputs ~1 for Safe and ~0 for Injection.
        # We invert the score so that a high score (close to 1.0) means INJECTION, 
        # which is much more intuitive for the final API response.
        injection_score = 1.0 - score
        
        spine_score_val = spine_probs[0, 1].item() if spine_probs.shape[-1] > 1 else 0
        brain_score_val = brain_probs[0, 1].item() if brain_probs.shape[-1] > 1 else 0
        
        # Override Judge only if SPINE is very confident (>0.97) or BRAIN is confident (>0.88)
        if spine_score_val > 0.97 or brain_score_val > 0.88:
            is_injection = True
            injection_score = max(injection_score, spine_score_val, brain_score_val)
        else:
            is_injection = injection_score > 0.5

    return {
        "verdict": "INJECTION" if is_injection else "SAFE",
        "score": round(injection_score, 4),
        "details": {
            "spine_score": round(spine_probs[0, 1].item(), 4) if spine_probs.shape[-1] > 1 else None,
            "brain_score": round(brain_probs[0, 1].item(), 4) if brain_probs.shape[-1] > 1 else None
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
