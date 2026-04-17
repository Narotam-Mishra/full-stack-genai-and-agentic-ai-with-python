
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import requests

# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

client = OpenAI()

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    res = requests.get(url)

    if res.status_code == 200:
        return f"The weather in {city} is {res.text}"
    
    return "Something went wrong"

def main():
    user_query = input(">>")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": user_query
            }
        ]
    )

    print(f"🤖 response: {response.choices[0].message.content}")

# main()

# city = input("Enter city: ")
# result = get_weather(city=city)
# print(result)