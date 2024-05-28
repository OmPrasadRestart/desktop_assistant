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
    

if __name__ == "__main__":
    query = takeCommand().lower()
    print(query)
    
    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'play music' in query:
        music_dir = 'F:\\iNeuron\\FSDS with GenAI\\desktop_assistant\\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'the time' in query:
    
            
