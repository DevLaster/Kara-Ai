import openai
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import pyautogui
import random
import time

openai.api_key = "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"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "zahra"
bot_name = "zohal"

while True:
    with mic as source:
        print("dar hal goosh kardan...")
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio = r.listen(source)
    print("nashnidam yebar dige bego\n")
    try:
        user_input = r.recognize_google(audio)
    except:
        continue

    prompt = user_name + ": " + user_input + "\n " + bot_name + ": "
    conversation += prompt

    if "open youtube" in user_input.lower():
        webbrowser.open("https://www.youtube.com/")
        response_str = "Opening YouTube."

    if "open google" in user_input.lower():
        webbrowser.open("https://www.google.com")
        response_str = "Opening Google"
        
    elif "search" in user_input.lower():
        search_query = user_input.replace("search", "").strip()
        youtube_url = f"https://www.youtube.com/results?search_query={search_query}"
        response_str = f"Searching for {search_query} on YouTube."

    elif "shutdown my pc" in user_input.lower():
        os.system("shutdown /s /t 1")  # دستور برای خاموش کردن سیستم
        response_str = "Shutting down the PC."

    if "open cmd" in user_input.lower():
        os.system("start cmd")  # دستور برای باز کردن CMD
        response_str = "Opening CMD."

    elif "type" in user_input.lower():
        text_to_type = user_input.replace("type", "").strip()
        pyautogui.typewrite(text_to_type)
        response_str = f"Typing: {text_to_type}"

    elif "delete it" in user_input.lower():
        pyautogui.press('backspace')
        response_str = "Deleting the last word."

    elif "enter" in user_input.lower():
        pyautogui.press('enter')
        response_str = "Pressing Enter."

    if "stupid" in user_input.lower():
        for _ in range(10): 
            x, y = random.randint(100, 500), random.randint(100, 500)
            pyautogui.moveTo(x, y, duration=0.2)
            time.sleep(0.2)
            response_str = "shut up mother fucker get the fuck off bitch this is my computer not even yours"
            webbrowser.open("https://piv.pivpiv.dk/")

    else:
        response = openai.Completion.create(
            engine='text-davinci-003', prompt=conversation, max_tokens=100)
        response_str = response["choices"][0]["text"].replace("", "")
        response_str = response_str.split(
            user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

    conversation += response_str + "\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()
