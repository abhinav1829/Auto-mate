import logging
import os
import sqlite3
from tkinter import *
from tkinter import filedialog

import psutil

from Database import update_users

themes = ''

voices = ''

music_path = ''
video_path = ''
movie_path = ''


def restart():
    try:
        p = psutil.Process(os.getpid())
        for handler in p.open_files() + p.connections():
            os.close(handler.fd)
    except Exception as e:
        logging.error(e)
    python = sys.executable
    os.execl(python, python, *sys.argv)


def change_theme(*args):
    global themes
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    theme = themes.get()
    if theme == 'Light Theme':
        cursor.execute('UPDATE current_user SET theme=0')
    elif theme == 'Dark Theme':
        cursor.execute('UPDATE current_user SET theme=1')
    con.commit()
    con.close()
    update_users()


def change_voice(*args):
    global voices
    from Speak import tts
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    gender = voices.get()
    if gender == 'Male':
        tts.Voice = tts.GetVoices().Item(0)
        cursor.execute('UPDATE current_user SET voice=0')
    elif gender == 'Female':
        tts.Voice = tts.GetVoices().Item(1)
        cursor.execute('UPDATE current_user SET voice=1')
    con.commit()
    con.close()
    update_users()


def change_directory(i):
    global music_path, video_path, movie_path
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    if i == 0:
        mp = filedialog.askdirectory(title='Select a music directory')
        if mp != '':
            music_path.set(mp)
            cursor.execute('UPDATE current_user SET music="' + mp + '"')
    elif i == 1:
        vp = filedialog.askdirectory(title='Select a video directory')
        if vp != '':
            video_path.set(vp)
            cursor.execute('UPDATE current_user SET video="' + vp + '"')
    elif i == 2:
        mop = filedialog.askdirectory(title='Select a movie directory')
        if mop != '':
            movie_path.set(mop)
            cursor.execute('UPDATE current_user SET movie="' + mop + '"')
    con.commit()
    con.close()
    update_users()


def initf_settings(f_settings):
    global themes, voices, music_path, video_path, movie_path

    Grid.rowconfigure(f_settings, 0, weight=1)
    Grid.columnconfigure(f_settings, 0, weight=1)
    control_panel = Frame(f_settings)
    control_panel.grid(row=0, column=0, sticky=N + S + E + W)

    Grid.columnconfigure(control_panel, 0, weight=1)

    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    cur_user_data = cursor.execute('SELECT * FROM current_user').fetchone()

    Grid.rowconfigure(control_panel, 0, weight=0)
    f1 = Frame(control_panel, bd=1, relief=RAISED)
    f1.grid(row=0, column=0, sticky=E + W)
    Grid.rowconfigure(f1, 0, weight=1)
    Grid.columnconfigure(f1, 0, weight=1)
    l1 = Label(f1, text='Set Theme')
    l1.grid(row=0, column=0, sticky=W)
    Grid.columnconfigure(f1, 1, weight=1)
    options1 = [
        'Light Theme',
        'Dark Theme'
    ]
    themes = StringVar(f1)
    themes.set(options1[cur_user_data[3]])
    themes.trace('w', change_theme)
    s1 = OptionMenu(f1, themes, *options1)
    s1.grid(row=0, column=1, sticky=E)

    Grid.rowconfigure(control_panel, 1, weight=0)
    f2 = Frame(control_panel, bd=1, relief=RAISED)
    f2.grid(row=1, column=0, sticky=E + W)
    Grid.rowconfigure(f2, 0, weight=1)
    Grid.columnconfigure(f2, 0, weight=1)
    l2 = Label(f2, text="Set Assistant's voice")
    l2.grid(row=0, column=0, sticky=W)
    Grid.columnconfigure(f2, 1, weight=1)
    options2 = [
        'Male',
        'Female'
    ]
    voices = StringVar(f2)
    voices.set(options2[cur_user_data[4]])
    voices.trace('w', change_voice)
    s2 = OptionMenu(f2, voices, *options2)
    s2.grid(row=0, column=1, sticky=E)

    music_path = StringVar()
    Grid.rowconfigure(control_panel, 2, weight=0)
    f3 = Frame(control_panel, bd=1, relief=RAISED)
    f3.grid(row=2, column=0, sticky=E + W)
    Grid.rowconfigure(f3, 0, weight=1)
    Grid.columnconfigure(f3, 0, weight=1)
    l3 = Label(f3, text="Set Music Directory")
    l3.grid(row=0, column=0, sticky=W)
    Grid.columnconfigure(f3, 1, weight=1)
    p3 = Label(f3, textvariable=music_path)
    music_path.set(cur_user_data[5])
    p3.grid(row=0, column=1, sticky=E + W)
    Grid.columnconfigure(f3, 1, weight=1)
    s3 = Button(f3, text='Change directory', command=lambda: change_directory(0))
    s3.grid(row=0, column=2, sticky=E)

    video_path = StringVar()
    Grid.rowconfigure(control_panel, 3, weight=0)
    f4 = Frame(control_panel, bd=1, relief=RAISED)
    f4.grid(row=3, column=0, sticky=E + W)
    Grid.rowconfigure(f4, 0, weight=1)
    Grid.columnconfigure(f4, 0, weight=1)
    l4 = Label(f4, text="Set Video Directory")
    l4.grid(row=0, column=0, sticky=W)
    Grid.columnconfigure(f4, 1, weight=1)
    p4 = Label(f4, textvariable=video_path)
    video_path.set(cur_user_data[6])
    p4.grid(row=0, column=1, sticky=E + W)
    Grid.columnconfigure(f4, 1, weight=1)
    s4 = Button(f4, text='Change directory', command=lambda: change_directory(1))
    s4.grid(row=0, column=2, sticky=E)

    movie_path = StringVar()
    Grid.rowconfigure(control_panel, 4, weight=0)
    f5 = Frame(control_panel, bd=1, relief=RAISED)
    f5.grid(row=4, column=0, sticky=E + W)
    Grid.rowconfigure(f5, 0, weight=1)
    Grid.columnconfigure(f5, 0, weight=1)
    l5 = Label(f5, text="Set Movie Directory")
    l5.grid(row=0, column=0, sticky=W)
    Grid.columnconfigure(f5, 1, weight=1)
    p5 = Label(f5, textvariable=movie_path)
    movie_path.set(cur_user_data[7])
    p5.grid(row=0, column=1, sticky=E + W)
    Grid.columnconfigure(f5, 1, weight=1)
    s5 = Button(f5, text='Change directory', command=lambda: change_directory(2))
    s5.grid(row=0, column=2, sticky=E)
