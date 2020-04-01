from tkinter import *
import sqlite3

flag = False
login_root = Tk()


def check_credentials(username_entry, password_entry):
    global flag
    flag = False
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    rows = cursor.execute('SELECT username,password FROM users WHERE username="' + username_entry + '"').fetchall()
    if len(rows) == 0:
        print('No such account')
    elif len(rows) == 1:
        if rows[0][1] == password_entry:
            flag = True
            login_root.destroy()
            cursor.execute('DELETE FROM current_user')
            cursor.execute('INSERT INTO current_user SELECT * FROM users WHERE username = "' + username_entry + '"')
            con.commit()
        else:
            print('Incorrect password')
    else:
        print('Database error: More than one users with same username found!')
    con.close()


def new_entry(username_entry, password_entry):
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    rows = cursor.execute('SELECT username,password FROM users WHERE username="' + username_entry + '"').fetchall()
    if len(rows) == 0:
        cursor.execute(
            'INSERT INTO users (username,password) VALUES ("' + username_entry + '", "' + password_entry + '")'
        )
        con.commit()
        print('Account created')
    elif len(rows) == 1:
        print('User already exists')
    else:
        print('Database error: More than one users with same username found!')
    con.close()


def del_entry(username_entry, password_entry):
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    rows = cursor.execute('SELECT username,password FROM users WHERE username="' + username_entry + '"').fetchall()
    if len(rows) == 0:
        print('No such account')
    elif len(rows) == 1:
        if rows[0][1] == password_entry:
            cursor.execute('DELETE FROM users WHERE username="' + username_entry + '"')
            con.commit()
            print('Account deleted')
        else:
            print('Incorrect password')
    else:
        print('Database error: More than one users with same username found!')
    con.close()


def login_initialize():
    login_root.title('Login')
    username_label = Label(login_root, text='Username : ')
    username_label.grid(row=0, column=0, sticky=N + S + E + W)
    password_label = Label(login_root, text='Password : ')
    password_label.grid(row=1, column=0, sticky=N + S + E + W)

    username_entry = Entry(login_root)
    username_entry.grid(row=0, column=1, sticky=N + S + E + W)
    password_entry = Entry(login_root, show='*')
    password_entry.grid(row=1, column=1, sticky=N + S + E + W)

    del_user_btn = Button(login_root, text='Del User',
                          command=lambda: del_entry(username_entry.get(), password_entry.get()))
    del_user_btn.grid(row=2, column=0, sticky=N + S + E + W)
    signup_btn = Button(login_root, text='Sign Up',
                        command=lambda: new_entry(username_entry.get(), password_entry.get()))
    signup_btn.grid(row=2, column=1, sticky=N + S + E + W)
    login_btn = Button(login_root, text='Login',
                       command=lambda: check_credentials(username_entry.get(), password_entry.get()))
    login_btn.grid(row=3, column=0, columnspan=2, sticky=N + S + E + W)
    login_root.mainloop()


def authenticate():
    global flag
    login_initialize()
    if flag:
        return True
    else:
        return False
