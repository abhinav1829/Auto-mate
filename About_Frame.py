from tkinter import *


def initf_about(f_about):
    Grid.rowconfigure(f_about, 0, weight=1)
    Grid.columnconfigure(f_about, 0, weight=1)
    about = Frame(f_about)
    about.grid(row=0, column=0, sticky=N + E + W + S)

    Grid.rowconfigure(about, 0, weight=1)
    Grid.columnconfigure(about, 0, weight=1)
    summary = Label(about, text="'Automate' is your virtual personal assistant. It is developed to ease your internet "
                                "access tasks while providing a human friendly experience. It can prove to be very "
                                "helpful for digitally-illiterate users as well as the people overloaded with work.")
    summary.grid(row=0, column=0, sticky=N + E + W + S)

    Grid.rowconfigure(f_about, 1, weight=4)
    Grid.columnconfigure(f_about, 0, weight=1)
    details = Frame(f_about)
    details.grid(row=1, column=0, sticky=N + E + W + S)

    Grid.rowconfigure(details, 0, weight=1)
    Grid.columnconfigure(details, 0, weight=1)
    maps = Frame(details)
    maps.grid(row=0, column=0)

    hk = Label(maps, text='Keyword')
    hk.grid(row=0, column=0)
    ha = Label(maps, text='Action')
    ha.grid(row=0, column=1)
    k = Label(maps, text='google')
    k.grid(row=1, column=0)
    a = Label(maps, text='Google search')
    a.grid(row=1, column=1)
    k = Label(maps, text='youtube')
    k.grid(row=2, column=0)
    a = Label(maps, text='Play Youtube')
    a.grid(row=2, column=1)
    k = Label(maps, text='wikipedia')
    k.grid(row=3, column=0)
    a = Label(maps, text='Search Wikipedia')
    a.grid(row=3, column=1)
    k = Label(maps, text='weather')
    k.grid(row=4, column=0)
    a = Label(maps, text='Weather forecast')
    a.grid(row=4, column=1)
    k = Label(maps, text='movie')
    k.grid(row=5, column=0)
    a = Label(maps, text='Play movies offline')
    a.grid(row=5, column=1)
    k = Label(maps, text='*general*')
    k.grid(row=6, column=0)
    a = Label(maps, text='General conversations')
    a.grid(row=6, column=1)

    Grid.rowconfigure(details, 0, weight=1)
    Grid.columnconfigure(details, 1, weight=1)
    contact = Label(details, text='Contact us\n\nEmail - abhinavdhoka@gmail.com\nPhone - 8208172335', justify=LEFT)
    contact.grid(row=0, column=1, sticky=N + E + W + S)
