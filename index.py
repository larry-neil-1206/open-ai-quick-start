from dotenv import load_dotenv
import os
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))
print(os.getenv("OPENAI_KEY"))

try:
  completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
      {"role": "system", "content": "You will be provided with a message."},
      {"role": "user", "content": "How are you?"}
    ],
    temperature=0.8,
    max_tokens=64,
    top_p=1
  )
  print(json.dumps(completion.dict(), indent=4))
except Exception as e:
  print(f"API key is invalid. Error: {e}")