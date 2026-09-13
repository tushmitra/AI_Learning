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
message = "Suggest me a good re-selling ticket website name."
message_system = "You are a creative business person who excels in marketing and branding suggest me a good name which can impact individuals in a single look suggest only a single name."
messages = [{"role": "system", "content": message_system}, {"role": role, "content": message}]
response = client.chat.completions.create(model=model, messages=messages, temperature=0.7)
print(response.choices[0].message.content)