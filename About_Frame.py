from tkinter import *


def initf_about(f_about):
    Grid.rowconfigure(f_about, 0, weight=1)
    Grid.columnconfigure(f_about, 0, weight=1)
    about = Label(f_about)
    about.grid(row=0, column=0, sticky=N + S + E + W)

    Grid.rowconfigure(about, 0, weight=1)
    Grid.columnconfigure(about, 0, weight=1)
    creators = Label(about, text="Created by -\n"
                                 "* Aadit Damle        4222\n"
                                 "* Abhinav Dhoka      4227\n"
                                 "* Pranit Shelke      4272\n"
                                 "* Shreyash Talwekar  4276\n", justify=LEFT)
    creators.grid(row=0, column=0, sticky=N + E + W)

    Grid.rowconfigure(about, 1, weight=1)
    Grid.columnconfigure(about, 0, weight=1)
    features = Label(about, text='KEYWORD      ACTION\n'
                                 '-------------------\n'
                                 'google       Google search\n'
                                 'wikipedia    Wikipedia search\n'
                                 'youtube      Play Youtube\n'
                                 'directions   Use maps\n'
                                 'gmail        Send email through Gmail\n'
                                 'weather      Get weather details\n', justify=LEFT)
    features.grid(row=1, column=0, sticky=N + E + W)
