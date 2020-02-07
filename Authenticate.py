from tkinter import *

flag = False
login_root = Tk()


def check_credentials(username_entry, password_entry):
    file = open('users', 'r')
    entries = file.readlines()
    file.close()

    global flag
    flag = False
    for entry in entries:
        if username_entry == entry.split(' ')[0]:
            flag = True
            if password_entry == entry.split(' ')[1].split('\n')[0]:
                login_root.destroy()
                return
            break
    if flag:
        print('Invalid password')
        flag = False
    else:
        print('Invalid username')


def new_entry(username_entry, password_entry):
    file = open('users', 'r')
    entries = file.readlines()
    file.close()

    for entry in entries:
        if username_entry == entry.split(' ')[0]:
            print('User already exists')
            return

    file = open('users', 'a')
    file.write(username_entry + " " + password_entry + "\n")
    file.close()
    print('Account created')


def del_entry(username_entry, password_entry):
    file = open('users', 'r')
    entries = file.readlines()
    file.close()

    global flag
    flag = False
    for entry in entries:
        if username_entry == entry.split(' ')[0] and password_entry == entry.split(' ')[1].split('\n')[0]:
            entries.remove(entry)
            print('Account deleted')
            flag = True
            break
    if not flag:
        print('No such account')
        return

    flag = False
    file = open('users', 'w')
    for entry in entries:
        file.write(entry)
    file.close()


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
