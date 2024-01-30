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
      {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
      {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
  )
  print(json.dumps(completion.dict(), indent=4))
except Exception as e:
  print(f"API key is invalid. Error: {e}")