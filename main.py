import pyttsx3
import datetime
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import requests, json
from colorama import Fore, Back, Style
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 2)


# we need it to talk duh
def speak(words):
    # words is what the bot will say
    engine.say(words)
    engine.runAndWait()


# function to welcome the user
def welcomeHome():
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak('Good Morning Jake!')
    elif (hour >= 12 and hour < 18):
        speak('Good Afternoon Jake!')
    elif (hour >= 18 and hour < 24):
        speak('Good Evening Jake!')
    else:
        speak('Goodnight Jake!')

    speak('This is Jake Bot, I can help you!')


# create the opening screen for the bot in the terminal
print(Fore.GREEN + '░░░░░██╗░█████╗░██╗░░██╗███████╗░░░░░░░░██████╗░░█████╗░████████╗░░░██████╗░██╗░░░██╗')
print(Fore.GREEN + '░░░░░██║██╔══██╗██║░██╔╝██╔════╝░░░░░░░░██╔══██╗██╔══██╗╚══██╔══╝░░░██╔══██╗╚██╗░██╔╝')
print(Fore.GREEN + '░░░░░██║███████║█████═╝░█████╗░░░░░░░░░░██████╦╝██║░░██║░░░██║░░░░░░██████╔╝░╚████╔╝░')
print(Fore.GREEN + '██╗░░██║██╔══██║██╔═██╗░██╔══╝░░░░░░░░░░██╔══██╗██║░░██║░░░██║░░░░░░██╔═══╝░░░╚██╔╝░░')
print(Fore.GREEN + '╚█████╔╝██║░░██║██║░╚██╗███████╗░░░░░░░░██████╦╝╚█████╔╝░░░██║░░░██╗██║░░░░░░░░██║░░░')
print(Fore.GREEN + '░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░░░░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝╚═╝░░░░░░░░╚═╝░░░')

# create a screen to tell people how awesome you are
print(Style.RESET_ALL)
print(Back.RED + 'THIS WAS MADE BY JAKE ANDREW FLAHERTY')
print(Back.RED + 'HIS EMAIL IS JAKEAFLAHERTY@YAHOO.COM')
print(Style.RESET_ALL)

welcomeHome()


# now we make the functions of the Jarvis bot (who i will call jake)


# change to a different voice
def voice_change(v):
    # v will be the number that changes voice it will be a number
    x = int(v)
    engine.setProperty('voice', voices[x].id)  # this is the same function we used up top
    # here we use the speak function
    speak('done user')


# function to tell you the date
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    daytime = int(datetime.datetime.now().day)
    # currently outputs numbers not month name we are fixing it now
    if (month == 1):
        monthname = 'January'
        speak(year)
        speak(monthname)
        speak(daytime)
    if (month == 2):
        monthname = 'Febuary'
        speak(year)
        speak(monthname)
        speak(daytime)
    if (month == 3):
        monthname = 'March'
        speak(year)
        speak(monthname)
        speak(daytime)
    if (month == 4):
        monthname = 'April'
        speak(year)
        speak(monthname)
        speak(daytime)
    if (month == 5):
        monthname = 'May'
        speak(year)
        speak(monthname)
        speak(daytime)
    if (month == 6):
        monthname = 'June'
        speak(year)
        speak(monthname)
        speak(daytime)
    if (month == 7):
        monthname = 'July'
        speak(year)
        speak(monthname)
        speak(daytime)
    if (month == 8):
        monthname = 'August'
        speak(year)
        speak(monthname)
        speak(daytime)
    if (month == 9):
        monthname = 'September'
        speak(year)
        speak(monthname)
        speak(daytime)
    if (month == 10):
        monthname = 'October'
        speak(year)
        speak(monthname)
        speak(daytime)
    if (month == 11):
        monthname = 'November'
        speak(year)
        speak(monthname)
        speak(daytime)
    if (month == 12):
        monthname = 'December'
        speak(year)
        speak(monthname)
        speak(daytime)

def birthday():
    speak('for my birthday say you, for my masters birthday say master')
    answer = takeCommand()
    if ('you' in answer):
        speak('My birthday is May 6')
    elif ('master' in answer):
        speak("jake's birthday is august 11")

def time():
    hour = int(datetime.datetime.now().hour)
    minnow = int(datetime.datetime.now().minute)
    speak('the time is currently ' + str(hour) + " and " + str(minnow))


# this is a closing function
def closing():
    speak('That is it for Jake Bot I will die now.')
    quit()


# how will it know what to do???
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('I am listening.')
        r.pause_threshold = 0.5  # this is in seconds
        spoke = r.listen(source)

    try:
        speak('Trying to understand now.')
        query = r.recognize_google(spoke, language='en=in')

    except Exception as e:
        print(e)
        speak('Say that again. I am having troubles hearing you.')

        return

    return query


# that was painful so hopefully it works!

def haha():
    j = pyjokes.get_joke()
    print(j)
    speak(j)


# im just gonna go on a spree of finding fun stuff to make it do

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU percentage is at ' + usage)


def temp():
    tempurature = psutil.sensors_temperatures()
    speak(tempurature)


def personal():
    speak(
        "I am Jake Bot, I was made by the great Jake from Wilson North Carolina and do not do much, currently this is version 2.0")


if __name__ == "__main__":
    while (True):

        if (takeCommand() is None):
            takeCommand()

        query = takeCommand().lower()


        if ('date' in query):
            date()

        elif ('who are you' in query or "about you" in query or "yourself" in query):
            personal()

        elif ('shutdown' in query):
            os.system("shutdown /r /t 1")

        elif ("cpu" in query or "usage" in query):
            cpu()

        elif ("tempurature" in query or "temps" in query):
            temp()

        elif ("tell me a joke" in query or "joke" in query):
            haha()

        elif ('voice' in query):
            speak('for female say female, and for male say man')
            q = takeCommand()
            if ('female' in q):
                voice_change(1)
            elif ('man' in q):
                voice_change(0)

        # if people dont like extra steps lol

        elif ("man" in query or "female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("man" in query):
                voice_change(0)

        elif ("time" in query):
            time()

        elif ('birthday' in query):
            birthday()

        # exit function

        elif ('i am done' in query or "bye bye" in query or "go offline" in query):
            closing()

            # attempt to add an option to have text answers []
