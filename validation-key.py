import openai

def check_openai_api_key(api_key):
    client = openai.OpenAI(api_key=api_key)
    try:
        print(client.models.list())
    except Exception as e:
      print(e)
      return False
    else:
        return True


api_key = "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"
is_valid = check_openai_api_key(api_key)

if is_valid:
    print("Valid OpenAI API key.")
else:
    print("Invalid OpenAI API key.")