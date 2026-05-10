import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

AMD_ENDPOINT = os.getenv("AMD_ENDPOINT", "http://127.0.0.1:8001/v1")
AMD_MODEL = os.getenv("AMD_MODEL", "Qwen/Qwen2.5-7B-Instruct")

print(f"Testing Qwen at: {AMD_ENDPOINT}")
print(f"Model: {AMD_MODEL}")

client = OpenAI(base_url=AMD_ENDPOINT, api_key="not-required")

try:
    response = client.chat.completions.create(
        model=AMD_MODEL,
        messages=[{"role": "user", "content": "Hello, are you working?"}],
        max_tokens=10
    )
    print("✅ Success!")
    print("Response:", response.choices[0].message.content)
except Exception as e:
    print("❌ Failed to connect to Qwen.")
    print("Error:", str(e))
