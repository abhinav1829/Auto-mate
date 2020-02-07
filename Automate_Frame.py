from tkinter import *
from Listen import listen


def initf_automate(f_automate):
    Grid.rowconfigure(f_automate, 0, weight=1)
    Grid.columnconfigure(f_automate, 1, weight=1)
    txt = Text(f_automate)
    txt.grid(row=0, column=1, sticky=N + S + E + W)

    Grid.rowconfigure(f_automate, 0, weight=1)
    Grid.columnconfigure(f_automate, 0, weight=1)
    panel = Frame(f_automate)
    panel.grid(row=0, column=0, sticky=N + S + E + W)

    Grid.rowconfigure(panel, 0, weight=1)
    Grid.columnconfigure(panel, 0, weight=1)
    listen_btn = Button(panel, text='Listen', command=lambda: listen(txt))
    listen_btn.grid(row=0, column=0, sticky=N + S + E + W)

    Grid.rowconfigure(panel, 1, weight=1)
    Grid.columnconfigure(panel, 0, weight=1)
    dummy = Frame(panel)
    dummy.grid(row=1, column=0, sticky=N + S + E + W)
