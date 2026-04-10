
# Implementing a Custom Tokenizer

import tiktoken

# returns the encoding obj used by a model
enc = tiktoken.encoding_for_model("gpt-4o")

# print("Enc", enc)

text = "Hey there! My name is Peter King"

# encodes a string into tokens.
tokens = enc.encode(text)

# Tokens: [25216, 1354, 0, 3673, 1308, 382, 16104, 8768]
print(f"Tokens: {tokens}")

decoded_text = enc.decode([25216, 1354, 0, 3673, 1308, 382, 16104, 8768])
print(f"decoded_text: {decoded_text}")
