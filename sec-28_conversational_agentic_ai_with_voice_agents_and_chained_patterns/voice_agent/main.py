
# speech to text

import speech_recognition as sr

def main():
    spr = sr.Recognizer()

    with sr.Microphone() as source:
        print("Calibrating... (stay quiet for 0.5s)")
        spr.adjust_for_ambient_noise(source, duration=0.5)  # shorter calibration
        
        # Debug: print what threshold was set
        print(f"Energy threshold set to: {spr.energy_threshold}")
        
        spr.pause_threshold = 2

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

main()