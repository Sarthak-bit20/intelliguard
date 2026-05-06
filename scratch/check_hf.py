from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

try:
    print("Attempting to load model...")
    tokenizer = AutoTokenizer.from_pretrained("sarthak20P/IntelliGuard-Brain-v3")
    model = AutoModelForSequenceClassification.from_pretrained("sarthak20P/IntelliGuard-Brain-v3")
    print("Success! Model and Tokenizer loaded.")
except Exception as e:
    print(f"Error: {e}")
