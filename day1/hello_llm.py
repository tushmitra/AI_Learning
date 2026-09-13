import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")
client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"
role = "user"
message = "Write a short poem about the beauty of nature."
messages = [{"role": role, "content": message}]
response = client.chat.completions.create(model=model, messages=messages)
print(response.choices[0].message.content)