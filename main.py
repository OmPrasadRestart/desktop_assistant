import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os

# Taking voice from my system

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# print(voices)
# print(type(voices))

# speak functions from my system

def speak(text):
    """This function takes a string and returns a voice

    Args:
        text (_type_): _description_
    """
    engine.say(text)
    engine.runAndWait()

# speak("Hello I am a programmer. How are you a programmer")

# speech recognition function
def takeCommand():
    """This function will record will recognize speech and return text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source_microphone:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source_microphone)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query
    

text= takeCommand()
speak(text)
    
            
