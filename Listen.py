import datetime
import os
import urllib
import webbrowser
from tkinter import *

import speech_recognition
import wikipedia

from Speak import speak

flag = True


def wish_me(txt):
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good  Morning", txt)
    elif 12 <= hour < 18:
        speak("Good afternoon", txt)
    else:
        speak("Good evening", txt)
    speak("I am automate . How may I help you ?", txt)


def take_command(txt):
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Listening....')
        txt.insert(INSERT, 'Listening....\n')
        txt.update()
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        txt.insert(INSERT, 'Recognizing...\n')
        txt.update()
        query = r.recognize_google(audio, language='en-in')
        print('User : ' + query + '\n')
        txt.insert(INSERT, 'User : ' + query + '\n')
        txt.update()
    except Exception as e:
        print(e)
        speak("Say again please...", txt)
        return 'none'
    return query


def listen(txt):
    global flag
    if flag:
        wish_me(txt)
        flag = False
    query = take_command(txt).lower()
    if 'youtube' in query:
        speak('Opening Youtube', txt)
        query = query.replace("youtube", "").strip().replace(" ", "+")
        htm_content = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + query)
        results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
        webbrowser.open("https://www.youtube.com/watch?v=" + results[0])
    elif 'wikipedia' in query:
        speak('searching wikipedia', txt)
        query = query.replace("wikipedia", "").strip()
        results = wikipedia.summary(query, sentences=2)
        speak('according to wikipedia', txt)
        print(results)
        speak(results, txt)
    elif 'google' in query:
        speak("Searching Google", txt)
        query = query.replace("google", "").strip()
        webbrowser.open('https://www.google.com/search?q=' + query)
    elif 'play movie' in query:
        speak('playing movie active measures .', txt)
        movie_dir = 'G:\Movies\Active Measures'
        movies = os.listdir(movie_dir)
        os.startfile(os.path.join(movie_dir, movies[0]))
    elif 'bye' in query:
        speak('Goodbye', txt)
        exit()
    elif query == 'none':
        pass
    else:
        speak('I am not sure about this', txt)
