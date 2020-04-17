import datetime

import Actions
from Input import take_command
from Speak import speak

flag = True


def wish_me(txt):
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning.", txt)
    elif 12 <= hour < 18:
        speak("Good afternoon.", txt)
    else:
        speak("Good evening.", txt)
    speak("I am automate. How may I help you?", txt)


def listen(txt):
    global flag
    if flag:
        wish_me(txt)
        flag = False

    dictionary = dict([('playmedia', ['play', 'music', 'mp3', 'song', 'video']),
                       ('movie', ['play', 'movie', 'movies']),
                       ('google', ['google', 'search', 'web', 'worldwideweb', 'internet']),
                       ('youtube', ['youtube', 'play', 'video', 'videos', 'entertainment']),
                       ('wikipedia', ['wikipedia', 'encyclopedia', 'search', 'article', 'articles']),
                       ('weather', ['weather', 'temperature', 'climate']),
                       ('news', ['news', 'headlines']),
                       ('daydatetime', ['day', 'date', 'time']),
                       ('horoscope', ['horoscope', 'fortune', 'luck']),
                       ('joke', ['joke', 'jokes', 'fun', 'funny']),
                       ('note', ['note', 'notes']),
                       ('repeat', ['repeat', 'sorry', 'pardon']),
                       ('bye', ['goodbye', 'bye', 'byebye', 'sayonara', 'exit', 'close', 'tata'])])

    score = dict([('playmedia', 0),
                  ('movie', 0),
                  ('google', 0),
                  ('youtube', 0),
                  ('wikipedia', 0),
                  ('news', 0),
                  ('weather', 0),
                  ('daydatetime', 0),
                  ('horoscope', 0),
                  ('joke', 0),
                  ('note', 0),
                  ('repeat', 0),
                  ('bye', 0)])

    query = take_command(txt).lower()
    words = query.split(' ')

    if words[0] == 'note' or words[0] == 'memorize':
        Actions.note(query, txt)
        return

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
