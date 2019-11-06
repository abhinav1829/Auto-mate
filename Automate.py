from tkinter import *
from tkinter import Text

from automate import listen
import datetime
import os
import re
import urllib
import webbrowser
import speech_recognition as sr
import wikipedia
from win32com.client import Dispatch

tts = Dispatch("SAPI.SpVoice")
root = Tk()


def initialize():
    root.title('Automate')
    root.state('zoomed')

    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)
    f = Frame(root)
    f.grid(row=0, column=0, sticky=N + S + E + W)

    Grid.rowconfigure(f, 1, weight=8)
    Grid.columnconfigure(f, 0, weight=1)

    f_settings = Frame(f)
    f_settings.grid(row=1, column=0, sticky=N + S + E + W)

    f_about = Frame(f)
    f_about.grid(row=1, column=0, sticky=N + S + E + W)

    f_automate = Frame(f)
    f_automate.grid(row=1, column=0, sticky=N + S + E + W)

    initf_automate(f_automate)
    initf_settings(f_settings)
    initf_about(f_about)

    Grid.rowconfigure(f, 0, weight=1)
    Grid.columnconfigure(f, 0, weight=1)
    f_menu = Frame(f)
    f_menu.grid(row=0, column=0, sticky=N + S + E + W)
    initf_menu(f_menu,f_automate,f_settings,f_about)

    pass


def initf_menu(f_menu, f_automate,f_settings,f_about):
    for row_index in range(1):
        Grid.rowconfigure(f_menu, row_index, weight=1)
        for col_index in range(3):
            Grid.columnconfigure(f_menu, col_index, weight=1)

    btn1 = Button(f_menu, text='Automate',command=f_automate.lift)
    btn1.grid(row=0, column=0, sticky=N + S + E + W)

    btn2 = Button(f_menu, text='Settings',command=f_settings.lift)
    btn2.grid(row=0, column=1, sticky=N + S + E + W)

    btn3 = Button(f_menu, text='About',command=f_about.lift)
    btn3.grid(row=0, column=2, sticky=N + S + E + W)
    pass


def initf_automate(f_automate):
    Grid.rowconfigure(f_automate, 0, weight=1)
    Grid.columnconfigure(f_automate, 1, weight=1)
    txt = Text(f_automate)
    txt.grid(row=0, column=1, sticky=N + S + E + W)

    Grid.rowconfigure(f_automate, 0, weight=1)
    Grid.columnconfigure(f_automate, 0, weight=1)
    btn4 = Button(f_automate, text='Listen', command=lambda: listen(txt))
    btn4.grid(row=0, column=0, sticky=N + S + E + W)

    pass


def initf_settings(f_settings):
    pass


def initf_about(f_about):
    pass


def speak(query, txt):
    txt.insert(INSERT, 'Automate : ')
    txt.insert(INSERT, query)
    txt.insert(INSERT, '\n')
    txt.update()
    tts.Speak(query)


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
    r = sr.Recognizer()
    with sr.Microphone() as source:
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
        return "None"
    return query


def listen(txt):
    wish_me(txt)
    query = take_command(txt).lower()
    if 'youtube' in query:
        speak('Opening Youtube', txt)
        query = query.replace("youtube", "").strip().replace(" ", "+")
        htm_content = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + query)
        results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
        webbrowser.open("https://www.youtube.com/watch?v=" + results[0])
    elif 'wikipedia' in query:
        speak('Searching Wikipedia', txt)
        query = query.replace("wikipedia", "").strip()
        results = wikipedia.summary(query, sentences=2)
        speak('According to wikipedia', txt)
        print(results)
        speak(results, txt)
    elif 'google' in query:
        speak("Searching Google", txt)
        query = query.replace("google", "").strip()
        webbrowser.open('https://www.google.com/search?q=' + query)
    elif 'play movie' in query:
        speak('Playing movie Active Measures .', txt)
        movie_dir = 'G:\Movies\Active Measures'
        movies = os.listdir(movie_dir)
        os.startfile(os.path.join(movie_dir, movies[0]))
    elif 'bye' in query:
        speak('Goodbye', txt)
        exit()


if __name__ == '__main__':
    initialize()
    root.mainloop()
