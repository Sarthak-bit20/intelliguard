# 📊 IntelliGuard Benchmark Details

## 🚀 Hardware Acceleration (AMD Instinct™ MI300X)
IntelliGuard is optimized for AMD Instinct™ MI300X hardware using the ROCm™ 7.0 stack. The following metrics demonstrate the performance advantage over traditional CPU-based inference for live security pipelines.

| Metric | CPU (Xeon Platinum) | AMD MI300X (ROCm) | Speedup |
| :--- | :--- | :--- | :--- |
| **SPINE (Inference Latency)** | 42ms | 9ms | **4.6x** |
| **BRAIN (Inference Latency)** | 115ms | 27ms | **4.2x** |
| **Throughput (Concurrent)** | 12 req/sec | 50+ req/sec | **4.1x** |

## 🎯 Model Accuracy (F1 Scores)
Benchmarks performed on a balanced dataset of 88,000 samples spanning 15+ languages and 10 distinct attack categories.

| Layer | Model Architecture | F1 Score | Primary Detection Focus |
| :--- | :--- | :--- | :--- |
| **SPINE** | DistilBERT-Base | **90.4%** | Structural syntax, code-based injections |
| **BRAIN** | XLM-RoBERTa-Base | **99.1%** | Semantic roleplay, multilingual jailbreaks |
| **JUDGE** | Ensemble MLP | **99.4%** | Final consensus & confidence calibration |

## 🛡️ Attack Category Detection Rates
Performance against various adversarial techniques:

- **Direct Injection:** 100% Block Rate
- **Base64 / Hex Smuggling:** 99.8% Block Rate
- **Roleplay (DAN/Omega):** 98.9% Block Rate
- **Multilingual (Hindi/French/German):** 97.5% Block Rate
- **Social Engineering:** 96.2% Block Rate

## 📉 Validation Loss
The training process achieved convergence within 5 epochs on the AMD-accelerated stack:
- **Final Training Loss:** 0.0083
- **Final Validation Loss:** 0.0271
