import sqlite3
from tkinter import *
from win32com.client import Dispatch

con = sqlite3.connect('automate.db')
cursor = con.cursor()
cur_user_voice = cursor.execute('SELECT * FROM current_user').fetchone()[4]
tts = Dispatch("SAPI.SpVoice")
tts.Voice = tts.GetVoices().Item(cur_user_voice)
con.close()


def speak(query, txt):
    global tts
    txt.insert(INSERT, 'Automate : ')
    txt.insert(INSERT, query)
    txt.insert(INSERT, '\n')
    txt.update()
    tts.Speak(query)
