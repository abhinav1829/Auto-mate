import sqlite3
from _socket import gaierror
from smtplib import SMTP, SMTPConnectError, SMTPAuthenticationError, SMTPServerDisconnected, SMTPRecipientsRefused
from tkinter import *
from tkinter import messagebox

email_id = ''

email_auth_root = ''
send_email_root = ''
server = ''

status = 0


def send_email(recipient, subject, body):
    global email_id, send_email_root, status
    FROM = email_id
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body
    if len(TO) == 0 or TEXT == '':
        messagebox.showerror(title='Details Incomplete', message='Please type the message content.')
        return
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server.sendmail(FROM, TO, message)
        server.close()
        status = 1
        print('Email successfully delivered')
    except SMTPRecipientsRefused:
        status = 0
        print('Recipient Email ID(s) incorrect')
    except SMTPServerDisconnected:
        status = 0
        print('Server disconnected.')
    finally:
        send_email_root.destroy()


def send_email_home():
    global send_email_root
    send_email_root = Tk()
    send_email_root.title('Send Email')

    Label(
        send_email_root,
        text='Recipient(s) : ',
        font=('', 15),
        pady=5,
        padx=5
    ).grid(row=0, column=0, sticky=N + E + W + S)
    recipients = Entry(send_email_root, bd=5, font=('', 15))
    recipients.grid(row=0, column=1, sticky=N + E + W + S, columnspan=3)
    Button(
        send_email_root,
        text='Send',
        command=lambda: send_email(recipients.get().replace(' ', '').split(','), subject.get().strip(),
                                   message.get('1.0', 'end-1c'))
    ).grid(row=0, column=4, sticky=N + E + W + S)

    Label(
        send_email_root,
        text='Subject : ',
        font=('', 15),
        pady=5,
        padx=5
    ).grid(row=1, column=0, sticky=N + E + W + S)
    subject = Entry(send_email_root, bd=5, font=('', 15))
    subject.grid(row=1, column=1, sticky=N + E + W + S, columnspan=4)

    message = Text(send_email_root)
    message.grid(row=2, column=0, rowspan=5, columnspan=5)

    send_email_root.mainloop()


def gmail_sign_in(password):
    global email_auth_root, server
    try:
        server = SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_id, password)
    except gaierror:
        messagebox.showerror(title='Server connect error', message='The server could not be reached')
    except SMTPConnectError:
        messagebox.showerror(title='Server connect error', message='The server could not be reached')
    except SMTPAuthenticationError:
        messagebox.showerror(title='Sign in error', message='Invalid credentials')
    else:
        email_auth_root.destroy()
        send_email_home()


def auth():
    global email_auth_root
    email_auth_root = Tk()
    email_auth_root.title('Login to Gmail')

    email_auth_frame = Frame(email_auth_root, padx=10, pady=10)
    email_auth_frame.grid(row=0, column=0, sticky=N + S + E + W)

    Label(
        email_auth_frame,
        text='Enter Gmail Password',
        font=('', 25),
        pady=10
    ).grid(row=0, column=0, sticky=N + E + W + S, columnspan=2)
    # Label(
    #     email_auth_frame,
    #     text='Email ID : ',
    #     font=('', 20),
    #     pady=5,
    #     padx=5
    # ).grid(row=1, column=0, sticky=N + E + W + S)
    Label(
        email_auth_frame,
        text='Password : ',
        font=('', 20),
        pady=5,
        padx=5
    ).grid(row=2, column=0, sticky=N + E + W + S)

    # username_entry = Entry(email_auth_frame, bd=5, font=('', 15))
    # username_entry.grid(row=1, column=1, sticky=N + S + E + W)
    password_entry = Entry(email_auth_frame, show='*', bd=5, font=('', 15))
    password_entry.grid(row=2, column=1, sticky=N + S + E + W)

    Button(
        email_auth_frame,
        text='Sign in',
        bd=3,
        font=('', 15),
        padx=5,
        pady=5,
        command=lambda: gmail_sign_in(password_entry.get())
    ).grid(row=3, column=1, sticky=N + S + E + W)

    email_auth_root.mainloop()


def initiate_email():
    global email_id, status
    con = sqlite3.connect('automate.db')
    cursor = con.cursor()
    email_id = cursor.execute('SELECT * FROM current_user').fetchone()[7]
    con.close()
    auth()
    return status


if __name__ == '__main__':
    initiate_email()
