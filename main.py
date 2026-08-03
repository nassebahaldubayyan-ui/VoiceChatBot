import os
import subprocess
from dotenv import load_dotenv
import cohere

from RealtimeSTT import AudioToTextRecorder


def speak(text):
    """Speaks text using Windows' built-in System.Speech synthesizer via
    PowerShell, run as a fresh subprocess each time. This avoids a known
    Windows issue where pyttsx3/SAPI5 hangs on the second call when reused
    within the same process."""
    escaped = text.replace('"', '`"')
    command = (
        "Add-Type -AssemblyName System.Speech; "
        f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{escaped}")'
    )
    subprocess.run(["powershell", "-Command", command])


def main():
    load_dotenv()

    co = cohere.Client(os.getenv("COHERE_API_KEY"))
    recorder = AudioToTextRecorder(model="tiny.en", language="en")

    print("Voice Assistant Started. Say 'exit' to quit.")

    try:
        while True:
            # 1. Speech to Text
            print("\nListening...")
            user_text = recorder.text()

            if not user_text:
                continue

            print(f"You: {user_text}")

            if user_text.lower().strip(".") in ["exit", "quit", "stop"]:
                break

            # 2. Generate response with LLM
            response = co.chat(
                model="command-a-03-2025",
                message=user_text,
            )
            assistant_reply = response.text
            print(f"Assistant: {assistant_reply}")

            # 3. Text to Speech
            recorder.use_microphone = False  # avoid mic picking up our own voice
            speak(assistant_reply)
            recorder.use_microphone = True
    finally:
        recorder.shutdown()


if __name__ == "__main__":
    main()