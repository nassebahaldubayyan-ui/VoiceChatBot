# Voice ChatBot 🎙️🤖

A real-time AI voice assistant built with Python. The chatbot listens to the user's voice, converts speech into text using Whisper, generates intelligent responses using Cohere's language model, and speaks the response back using Windows built-in text-to-speech.

## Features

- Real-time speech recognition
- AI-generated responses using Cohere LLM
- Text-to-speech voice responses
- Continuous conversation loop
- Voice command to stop the assistant
- Secure API key configuration using `.env`

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| OpenAI Whisper | Speech recognition model |
| RealtimeSTT | Real-time microphone speech-to-text |
| Cohere API | AI response generation |
| python-dotenv | Environment variable management |
| PowerShell System.Speech | Text-to-speech |
| SoundDevice | Audio input handling |
| SciPy | Audio processing |

---

# Requirements

## Operating System

- Windows

## Python Environment

This project was developed using an Anaconda environment

## Required API

- Cohere API Key

---

# Installation

## 1. Activate the Conda Environment

---

## 2. Install Dependencies

Install all packages:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install openai-whisper
pip install RealtimeSTT
pip install RealtimeTTS
pip install cohere
pip install python-dotenv
pip install sounddevice
pip install scipy
```

---

# API Key Setup

The chatbot requires a Cohere API key.

Create a file named:

```
.env
```

inside the project folder.

Add your personal API key:

```env
COHERE_API_KEY=your_api_key_here
```

Replace:

```
your_api_key_here
```

with your own Cohere API key.

Do not upload the `.env` file to GitHub because it contains private credentials.

---

# Running the ChatBot

Start the assistant using:

```bash
python main.py
```

You should see:

```
Voice Assistant Started. Say 'exit' to quit.
```

---

# How It Works

The chatbot follows three main steps:

## 1. Speech-to-Text

The microphone listens for user input.

The `RealtimeSTT` library uses Whisper (`tiny.en` model) to convert speech into text.

Example:

```
User speaks:
"What is artificial intelligence?"

Converted text:
"What is artificial intelligence?"
```

---

## 2. AI Response Generation

The converted text is sent to Cohere's language model:

```python
response = co.chat(
    model="command-a-03-2025",
    message=user_text,
)
```

Cohere generates a response based on the user's question.

---

## 3. Text-to-Speech

The generated response is converted into speech using Windows PowerShell:

```python
System.Speech.Synthesis.SpeechSynthesizer
```

A new PowerShell process is created every time the assistant speaks.

This avoids a Windows SAPI5 issue where speech engines can freeze after multiple uses in the same process.

---

# Exit Commands

The assistant stops when the user says:

```
exit
quit
stop
```

---

# First Run Note

The first execution downloads the Whisper:

```
tiny.en
```

model.

This may take a few minutes depending on internet speed.

---

# Important Notes

- A working microphone is required.
- Internet connection is required because Cohere runs through an API.
- Keep your API key private.
- The chatbot currently supports English speech recognition.

---

# Future Improvements

Possible improvements:

- Add conversation memory
- Add a graphical user interface
- Add wake-word activation ("Hey Assistant")
- Support more languages
- Add custom voices
- Add local AI model support

---

# 👩‍💻 Author

**Nassebah Al-Dubayyan**