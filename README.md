# IntelliGuard 🛡️
A 4-layer prompt injection detection pipeline protecting enterprise RAG systems.

## Architecture
Input → SPINE (DistilBERT) → DECODER → BRAIN (XLM-RoBERTa) → JUDGE → EXECUTOR

## Performance
- SPINE: 90.4% F1
- BRAIN: 99.1% F1  
- Dataset: 17,132 samples, 10 attack levels, 15+ languages, 13 encoding types

## Stack
- PyTorch + HuggingFace Transformers
- FastAPI
- ChromaDB + Groq LLM
- AMD ROCm (MI300X inference)

## Run API
```
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
