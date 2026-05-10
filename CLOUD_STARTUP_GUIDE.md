# 🚀 IntelliGuard: AMD Cloud Startup Guide

This guide documents the exact process for establishing the connection between the local IntelliGuard Portal and the remote Qwen vLLM instance on the AMD GPU Cloud.

---

## 🛠️ Step 1: Establish the SSH Tunnel (Windows PowerShell)
Open a **new** PowerShell window on your local machine and run the following command. **Keep this window open.**

```powershell
ssh -i C:\Users\SANAD\.ssh\amd_key3 -L 8001:localhost:30000 root@129.212.182.84
```
*   **Port 8001:** Local access point for the portal.
*   **Port 30000:** Remote port inside the cloud container.

---

## ☁️ Step 2: Cloud Container Setup (Remote Terminal)
Once logged into the remote server, perform these steps to prepare the environment:

1.  **Enter the Docker Container:**
    ```bash
    docker exec -it rocm /bin/bash
    ```

2.  **Kill Pre-installed Services (Free Port 80 & Memory):**
    ```bash
    pkill -9 jupyter
    pkill -9 python
    ```

3.  **Clear Stale vLLM Cache:**
    ```bash
    rm -rf /root/.cache/vllm
    ```

---

## 🧠 Step 3: Launch the Qwen AI Server
Inside the container, run the vLLM server. We use **Offline Mode** to skip redundant downloads and **Port 30000** for reliable tunneling.

```bash
export HF_HUB_OFFLINE=1
vllm serve Qwen/Qwen2.5-7B-Instruct --port 30000
```
**Wait for:** `Application startup complete.`

---

## 🧪 Step 4: Verification
To ensure everything is working, run these tests on your **Local Windows Machine**:

1.  **API Check (Browser or Terminal):**
    *   URL: [http://localhost:8001/v1/models](http://localhost:8001/v1/models)
    *   Should return JSON data.

2.  **IntelliGuard Portal:**
    *   Refresh: [http://localhost:8501](http://localhost:8501)
    *   Ask a question to see live logs in the cloud terminal.

---

## 🆘 Troubleshooting: "GPU Memory Full"
If you see `ValueError: Free memory on device cuda:0 is less than desired`, the GPU is locked by a ghost process.

**The Fix:**
1.  Exit the container (`exit`).
2.  Restart the container: `docker restart rocm`.
3.  Repeat **Step 2** and **Step 3**.

---

**IntelliGuard Security Pipeline:**
Local SPINE (Detection) -> Local BRAIN (Filtering) -> Remote Qwen (Inference)
