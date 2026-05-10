import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def test_qwen_chat():
    url = "http://127.0.0.1:8001/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    
    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello Qwen! If you can hear me, please tell me what's the weather like in the world of AI today?"}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }

    print(f"🚀 Sending test chat request to Qwen via tunnel...")
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)
        if response.status_code == 200:
            result = response.json()
            answer = result['choices'][0]['message']['content']
            print("\n✅ Qwen is ALIVE and responding!")
            print(f"\nQwen's Response: \"{answer}\"")
        else:
            print(f"\n❌ Qwen returned an error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"\n❌ Failed to reach Qwen: {e}")

if __name__ == "__main__":
    test_qwen_chat()
