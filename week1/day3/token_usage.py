import os

from dotenv import load_dotenv
from groq import Groq


# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)


# Model
model = "openai/gpt-oss-120b"

# Role
role = "user"


# Prompts
prompt1 = "What is Python?"
prompt2 = "Explain the difference between supervised and unsupervised learning."
prompt3 = "How does a large language model generate a response to a user's question?"

prompts = [prompt1, prompt2, prompt3]


# Send each prompt and check token usage
for prompt in prompts:

    message = {
        "role": role,
        "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=500
    )

    usage = response.usage

    print("\n" + "=" * 80)

    print(f"Prompt: {prompt}")

    print(f"Prompt tokens: {usage.prompt_tokens}")

    print(f"Completion tokens: {usage.completion_tokens}")

    print(f"Total tokens: {usage.total_tokens}")

    print(f"Finish reason: {response.choices[0].finish_reason}")

    print(f"Response: {response.choices[0].message.content}")

    print("=" * 80)