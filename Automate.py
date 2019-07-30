import datetime
import os
import re
import urllib
import webbrowser
import pygame

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good  Morning, Vishrut")
    elif 12 <= hour < 18:
        speak("Good afternoon, Vishrut")
    else:
        speak("Good evening, Vishrut")
    # speak("I am jarvis, your new assistant, Please tell me how may i help you")


def takecommand():
    # takes voice input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        speak("Say again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak('Opening youtube')
            query = query.replace("youtube", "")
            query = query.replace(" ", "")
            htm_content = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + query)
            results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
            webbrowser.open("https://www.youtube.com/watch?v=" + results[0])

        elif 'google' in query:
            query = query.replace(" ", "")
            webbrowser.open("https://www.google.com/search?q=" + query.replace("google", ""))

        elif 'play movie' in query:
            movie_dir = 'H:\\Movies\\Ant Man'
            movies = os.listdir(movie_dir)
            print(movies)
            os.startfile(os.path.join(movie_dir, movies[0]))
        elif 'music' in query:
            speak('Playing Music')
            query = query.replace("soundcloud","")
            query = query.replace(" ","")
            htm_content = urlib.request.urlopen('')
