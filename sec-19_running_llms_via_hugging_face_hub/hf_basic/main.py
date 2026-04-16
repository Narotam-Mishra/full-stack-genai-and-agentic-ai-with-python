
from transformers import pipeline

pipe = pipeline(
    "image-text-to-text",
    model="google/gemma-3-4b-it",
    trust_remote_code=True          # add this for newer models
)

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"
            },
            {
                "type": "text",
                "text": "What animal is on the candy?"
            }
        ]
    }
]

# Fix: capture the output, don't print messages (messages is just your input)
output = pipe(text=messages, max_new_tokens=200)

print(output[0]["generated_text"])