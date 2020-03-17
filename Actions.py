import os
import urllib
import webbrowser
from datetime import datetime
from tkinter import *
import GeneralConversations

import pyowm
import wikipedia as wiki
from horoscope_generator import HoroscopeGenerator

from Speak import speak

joke_count = 0


def general_conversation(query, txt):
    dictionary = dict([('who_are_you', ['who', 'are', 'you']),
                       ('toss_coin', ['heads', 'tails', 'flip', 'toss', 'coin']),
                       ('how_am_i', ['how', 'am', 'i', 'look', 'looking']),
                       ('who_am_i', ['who', 'am', 'i']),
                       ('where_born', ['how', 'where', 'you', 'born', 'birth']),
                       ('how_are_you', ['how', 'are', 'you']),
                       ('are_you_up', ['you', 'up']),
                       ('love_you', ['love', 'you']),
                       ('marry_me', ['marry', 'me'])])

    score = dict([('who_are_you', 0),
                  ('toss_coin', 0),
                  ('how_am_i', 0),
                  ('who_am_i', 0),
                  ('where_born', 0),
                  ('how_are_you', 0),
                  ('are_you_up', 0),
                  ('love_you', 0),
                  ('marry_me', 0)])

    words = query.split(' ')

    for word in words:
        for keyword in dictionary:
            for value in dictionary.get(keyword):
                if word == value:
                    score[keyword] += 1
                    break

    max_score = max(score, key=score.get)

    if score.get(max_score) == 0:
        speak('I am not sure about this', txt)
    else:
        getattr(GeneralConversations, max_score)(query, txt)


def google(query, txt):
    speak("Searching Google", txt)
    query = query.replace("google", "").strip()
    webbrowser.open('https://www.google.com/search?q=' + query)


def youtube(query, txt):
    speak('Opening Youtube', txt)
    query = query.replace("youtube", "").strip().replace(" ", "+")
    htm_content = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + query)
    results = re.findall('href=\"\\/watch\\?v=(.{11})', htm_content.read().decode())
    webbrowser.open("https://www.youtube.com/watch?v=" + results[0])


def wikipedia(query, txt):
    try:
        speak('searching wikipedia', txt)
        query = query.replace("wikipedia", "").strip()
        results = wiki.summary(query, sentences=2)
        speak('according to wikipedia', txt)
        speak(results, txt)
    except Exception as e:
        speak(e, txt)


def weather(query, txt):
    owm = pyowm.OWM('61cf9c73e72fb837f80c3e97ecd03a37')
    report = owm.weather_at_place('Pune')
    result = report.get_weather()
    detailed_status = result.get_detailed_status()
    temp = result.get_temperature(unit='celsius')
    weather_result = 'It is ' \
                     + detailed_status + ' in Pune. The temperature is ' \
                     + str(temp.get('temp')) + ' degrees celsius'
    speak(weather_result, txt)


def daydatetime(query, txt):
    if 'time' in query:
        speak("The time is " + datetime.strftime(datetime.now(), '%H:%M:%S'), txt)
    if 'date' in query:
        speak("The date is " + datetime.strftime(datetime.now(), '%m/%d/%Y'), txt)
    if 'day' in query:
        speak("The day is " + datetime.strftime(datetime.now(), '%A'), txt)


def horoscope(query, txt):
    speak((HoroscopeGenerator.format_sentence(HoroscopeGenerator.get_sentence())), txt)


def joke(query, txt):
    global joke_count
    jokes = [
        'What happens to a frogs car when it breaks down? It gets toad away.',
        'Why was six scared of seven? Because seven ate nine.',
        'Why are mountains so funny? Because they are hill areas.',
        'Have you ever tried to eat a clock?'
        'I hear it is very time consuming.',
        'What happened when the wheel was invented? A revolution.',
        'What do you call a fake noodle? An impasta!',
        'Did you hear about that new broom? It is sweeping the nation!',
        'What is heavy forward but not backward? Ton.',
        'No, I always forget the punch line.'
    ]
    speak(jokes[joke_count], txt)
    joke_count += 1


def bye(query, txt):
    speak('Goodbye', txt)
    os.system("taskkill /im chrome.exe")
    exit()
