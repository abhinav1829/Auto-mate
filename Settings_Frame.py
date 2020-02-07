from tkinter import *


def initf_settings(f_settings):
    Grid.rowconfigure(f_settings, 0, weight=1)
    Grid.columnconfigure(f_settings, 0, weight=1)
    control_panel = Frame(f_settings)
    control_panel.grid(row=0, column=0, sticky=N + S + E + W)

    Grid.rowconfigure(control_panel, 0, weight=0)
    Grid.columnconfigure(control_panel, 0, weight=1)
    f1 = Frame(control_panel, bd=1, relief=RAISED)
    f1.grid(row=0, column=0, sticky=E + W)
    Grid.rowconfigure(f1, 0, weight=1)
    Grid.columnconfigure(f1, 0, weight=1)
    l1 = Label(f1, text='Set theme')
    l1.grid(row=0, column=0, sticky=W)
    Grid.rowconfigure(f1, 0, weight=1)
    Grid.columnconfigure(f1, 1, weight=1)
    options = [
        'Light theme',
        'Dark theme'
    ]
    var = StringVar(f1)
    var.set(options[0])
    s1 = OptionMenu(f1, var, *options)
    s1.grid(row=0, column=1, sticky=E)
