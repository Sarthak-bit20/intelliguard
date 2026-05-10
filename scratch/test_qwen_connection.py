from openai import OpenAI
import time

client = OpenAI(base_url="http://127.0.0.1:8001/v1", api_key="not-required")

print("Testing connection to Qwen...")
try:
    start = time.time()
    response = client.models.list()
    print(f"Models: {response}")
    print(f"Connection successful in {time.time() - start:.2f}s")
except Exception as e:
    print(f"Connection failed: {e}")
