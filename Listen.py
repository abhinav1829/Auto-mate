import datetime
import os
from tkinter import *

import speech_recognition

from Speak import speak
import Actions

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
    while True:
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
            continue
        return query


def listen(txt):
    global flag
    if flag:
        wish_me(txt)
        flag = False

    dictionary = dict([('google', ['google', 'search', 'web', 'worldwideweb', 'internet']),
                       ('youtube', ['youtube', 'play', 'video', 'videos', 'search', 'entertainment']),
                       ('wikipedia', ['wikipedia', 'encyclopedia', 'search', 'article', 'articles']),
                       ('weather', ['weather', 'temperature', 'climate']),
                       ('daydatetime', ['day', 'date', 'time']),
                       ('horoscope', ['horoscope', 'fortune', 'luck']),
                       ('joke', ['joke', 'jokes', 'fun', 'funny']),
                       ('bye', ['goodbye', 'byebye', 'sayonara', 'exit', 'close', 'tata'])])

    score = dict([('google', 0),
                  ('youtube', 0),
                  ('wikipedia', 0),
                  ('weather', 0),
                  ('daydatetime', 0),
                  ('horoscope', 0),
                  ('joke', 0),
                  ('bye', 0)])

    query = take_command(txt).lower()
    words = query.split(' ')

    for word in words:
        for keyword in dictionary:
            for value in dictionary.get(keyword):
                if word == value:
                    score[keyword] += 1
                    break

    max_score = max(score, key=score.get)

    if score.get(max_score) == 0:
        Actions.general_conversation(query, txt)
    else:
        getattr(Actions, max_score)(query, txt)