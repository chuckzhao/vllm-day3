# vllm_stream_test.py
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",  # DIRECT TO vLLM
    api_key="sk-FAKE"
)

stream = client.chat.completions.create(
    model="hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4",
    messages=[{"role": "user", "content": "Say: Chuck got 100% reliable streaming with vLLM's official client on Day 3!"}],
    max_tokens=100,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print("\n\nSTREAMING COMPLETE!")
