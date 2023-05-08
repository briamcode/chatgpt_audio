import speech_recognition as sr
import pyttsx3
import openai
import os
import time
from gtts import gTTS

# Ubuntu
# sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
# pip install pyaudio

# Configurar el modelo de OpenAI
openai.api_key = "Tu_key_de_openai"
model_engine = "text-davinci-003"

# Configurar la biblioteca de síntesis de voz
engine = pyttsx3.init()



# Función para generar una respuesta de ChatGPT
def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
    )
    return response.choices[0].text.strip()

# Función para escuchar la entrada de voz del usuario
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10)
        try:
            text = recognizer.recognize_google(audio, language="es-CO")
            print(f"Entendido: {text}")
            return text.lower()
        except:
            print("No se pudo entender. Por favor, inténtalo de nuevo.")
            return ""

# Función para decir la respuesta de ChatGPT en voz alta
# Configurar la biblioteca de síntesis de voz
engine = pyttsx3.init('espeak')

def speak(text):
    tts = gTTS(text=text, lang='es')
    tts.save("response.mp3")
    os.system("mpg123 response.mp3")
    os.remove("response.mp3")

# Función para interactuar con ChatGPT por voz
def chat():
    while True:
        prompt = listen()
        if "adiós" in prompt:
            break
        if prompt:
            response = generate_response(prompt)
            print(response)
            speak(response)

if __name__ == "__main__":
    chat()
