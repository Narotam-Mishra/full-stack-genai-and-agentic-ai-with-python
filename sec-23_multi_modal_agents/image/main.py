
from pathlib import Path
from dotenv import load_dotenv

# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Generate caption for this image in 50 words"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://images.pexels.com/photos/879109/pexels-photo-879109.jpeg"
                    }
                },
            ],
        }
    ],
)

print(f"Response: {response.choices[0].message.content}")
