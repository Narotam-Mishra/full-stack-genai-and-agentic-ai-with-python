
# speech to text (open ai completion)

from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

import speech_recognition as sr
from openai import OpenAI
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer
import asyncio

client = OpenAI()

# async openai client
async_client = AsyncOpenAI()

async def tts(speech: str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        instructions="Always speak in cheerful manner with full of delight and happiness",
        input=speech,
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)


def main():
    # speech to text recognizer
    spr = sr.Recognizer()

    # get mic access
    with sr.Microphone() as source:
        print("Calibrating... (stay quiet for 0.5s)")
        spr.adjust_for_ambient_noise(source, duration=0.5)  # shorter calibration
        
        # Debug: print what threshold was set
        print(f"Energy threshold set to: {spr.energy_threshold}")

        # pause for 2 seconds then start recognition
        spr.pause_threshold = 2

        SYSTEM_PROMPT = f"""
            You're an expert voice agent. You are given the transcript of what user has said using voice.
            You need to output as if you are an voice agent and whatever you speak will be converted back to audio using AI and played back to user.
        """

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
        ]

        while True:

            print("Speak something...")
            try:
                audio = spr.listen(source, timeout=7, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                print("No speech detected. Try lowering energy_threshold manually.")
                return

            print("Processing Audio... (STT)")
            try:
                stt = spr.recognize_google(audio)
                print("You said:", stt)
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"API error: {e}")

                # Now wrap the AI response generation
            try:
                messages.append(
                    {"role": "user", "content": stt}
                )

                response = client.chat.completions.create(
                    model="gpt-4o-mini",  # Note: I assume this is a typo for "gpt-4o-mini" based on common models; adjust if needed
                    messages=messages
                )

                print(f"AI Voice Response: {response.choices[0].message.content}")
                
                # run tts task
                asyncio.run(tts(speech=response.choices[0].message.content))
            except Exception as e:  # Catch OpenAI or other errors
                print(f"Error generating AI response: {e}")


main()