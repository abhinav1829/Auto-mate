from tkinter import *
from win32com.client import Dispatch

tts = Dispatch("SAPI.SpVoice")


def speak(query, txt):
    global tts
    txt.insert(INSERT, 'Automate : ')
    txt.insert(INSERT, query)
    txt.insert(INSERT, '\n')
    txt.update()
    tts.Speak(query)
