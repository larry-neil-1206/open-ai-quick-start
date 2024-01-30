import openai
import os

def check_openai_api_key(api_key):
    client = openai.OpenAI(api_key=api_key)
    try:
        print(client.models.list())
    except Exception as e:
      print(e)
      return False
    else:
        return True


api_key = os.getenv("OPENAI_KEY")
is_valid = check_openai_api_key(api_key)

if is_valid:
    print("Valid OpenAI API key.")
else:
    print("Invalid OpenAI API key.")