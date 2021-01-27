import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from random import *
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Afternoon Sir!")
    else:
        speak("Good evening Sir!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening sir...")
        r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("User said:{}".format(query))
        except Exception as e:
            print("Sorry sir can you say that again please")
            return "None"
        return query


if __name__ == '__main__':

    query = takeCommand().lower()
    if 'jarvis' in query:
        wishme()
        while True:
            speak("how may I help you")
            #while True:
            # logic for executing task based on query
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to wikipedia...")
                print(results)
                speak(results)
            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com/")
            elif 'open google' in query:
                webbrowser.open("https://www.google.com/")
            elif 'open stackoverflow' in query:
                webbrowser.open("https://stackoverflow.com/")
            elif 'music' in query:
                music_dir = 'D:\\Music\\Hybrid Theory'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[randint(1, 5)]))
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak("Sir the time is{}".format(strTime))
            elif 'how are you' in query:
                speak("As always sir")
            elif "tony's database" in query:
                speak("You are not authorized to access his database...")
            elif "avengers theme" in query:
                playsound("D:\\Music\\avengers\\The-Avengers-Theme-Song.mp3")
            elif "marvels theme" in query:
                playsound("D:\\Music\\avengers\\The-Avengers-Theme-Song.mp3")
            elif "your favourite song" in query:
                speak("this is my all time favourite sir")
                playsound("D:\\Music\\avengers\\The-Avengers-Theme-Song.mp3")
            elif 'jarvis are you up' in query:
                speak("For you sir, always")
            elif 'thank you' in query:
                speak("no problem sir")
            elif 'do you miss tony' in query:
                speak("obviously sir...a lot")
            elif 'shutdown jarvis' in query:
                break
            elif 'shut down jarvis' in query:
                break
            elif 'jarvis shutdown' in query:
                break
            elif 'shut down jarvis' in query:
                break
            elif 'shutdown' in query:
                break
    else:
        speak("Sir are you talking to me...You can call me jarvis")