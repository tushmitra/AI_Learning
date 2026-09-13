# # import tiktoken

# # text = "Hello, I am learning about tokens and LLMs."

# # encoding = tiktoken.get_encoding("cl100k_base")

# # tokens = encoding.encode(text)

# # print("Text:", text)
# # print("Tokens:", tokens)
# # print("Number of tokens:", len(tokens))

# # print("\nDecoded tokens:")
# # for token in tokens:
# #     print(token, "->", repr(encoding.decode([token])))


# import tiktoken

# encoding = tiktoken.get_encoding("cl100k_base")

# texts = [
#     "Hello",
#     "Hello, how are you?",
#     "I am learning Python.",
#     "Artificial Intelligence and Machine Learning",
# ]

# for text in texts:
#     tokens = encoding.encode(text)

#     print(f"Text: {text}")
#     print(f"Tokens: {tokens}")
#     print(f"Token count: {len(tokens)}")
#     print("-" * 50)

import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

text = """
Large language models process text by breaking it into smaller pieces
called tokens. These tokens are then converted into numbers that the
model can process. Token count is important because API usage and
context limits are usually measured in tokens.
"""

tokens = encoding.encode(text)

print("Number of characters:", len(text))
print("Number of tokens:", len(tokens))
print("First 20 tokens:", tokens[:20])
print("\nToken pieces:")

for token in tokens:
    print(repr(encoding.decode([token])))