from pyttsx3 import speak
import speech_recognition as sr
import wikipedia
import webbrowser
import sys
import os
import cv2
import requests
import json
import playsound
import psutil
import random 
import bluetooth
import datetime
from datetime import date, time
from pynotifier import Notification    
from pyautogui import *
from win10toast import ToastNotifier

def wishme():
    hour = int(datetime.datetime.now().strftime("%H"))
    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon")
    else:
        speak("good evening")

def time_now():
    h = datetime.datetime.now().strftime("%H")
    m = datetime.datetime.now().strftime("%M")
    a = list(h)
    b = list(m)
    
    if a[0] == '0':
        a.remove('0')
        time_hour = str(a)
    elif int(h) >= 13:
        time_hour = int(h) - 12
    else:
        time_hour = h

    if b[0] == '0':
        b.remove('0')
        time_min = str(b)
    else:
        time_min = m

    speak(f"the time is {time_hour} {time_min}")  

def date_today():
    Date = date.today()
    speak(f"today's date is {Date}")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound.playsound("start.mp3")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        playsound.playsound("stop.mp3")
        query = r.recognize_google(audio,language = 'en-in')
    
    except Exception as e:
        print(e)
        speak("say that again please")
        return "None"
    return query

def reminder():
    alarm_time = input("Enter time ( HH:MM ) use 24hrs format = ")
    message = input("Type the purpose of the alarm = ")

    while True:
        current_time = datetime.now().strftime("%H:%M")

        if alarm_time == current_time:
            notification = ToastNotifier()
            notification.show_toast("Alarm", message, duration = 50)
            playsound.playsound("Marvel Theme.mp3")
            break

def bluetooth_devices():
    a = bluetooth.discover_devices(lookup_names = True)

    # uncomment the below loop to print the address and name of the devices
    '''for details in a:
        print("Address :", details[0])     
        print("Name :", details[1])'''
    
    total = []
    for i in a:
        total.append(i)

    # uncomment the below loop to print the name of the devices
    '''for j in range(0, len(total)):
        print(total[j][1])'''

    speak("yeah buddy, i have found, do you want me to tell the names")
    devices = command().lower()
    if devices in ["yes", "show me", "yes show me", "yeah"]:
        for n in range(0, len(total)):
            speak(f"they are, {total[n][1]}")
        speak("thats all buddy")
    else:
        speak("done buddy")
    
percent = ""
def battery_percentage():
    global percent
    battery = psutil.sensors_battery()
    percent = battery.percent
    speak(f"my energy level is {percent} percentage")

if __name__ == "__main__":
    while True:
        print("Activating  mark 3.... ")
        speak("Activating, mark 3")
        speak("just a moment")
        speak("hey buddy")
        wishme()
        date_today()
        time_now()
        battery_percentage()
        speak("Now tell me buddy, how can i help you")
        while True:
            if percent <= 20:
                speak(f"my energy level is getting low, its just {percent} percentage only")
                speak("i am gonna die, please connect charger")
                speak("or else i'll shutdown")
                
            query = command().lower()

            a = query.split(' ')
            for i in a:
                if i in ["buddy", "bro", "brother", "friend"]:
                    a.remove(i)

            query = ' '.join(a)

            if query in ["are you listening or not", "listening or not", "concentrate here"]:
                speak("yeah buddy, i am listening")

            elif query in ["what are you doing", "what's going on", "what's happening"]:
                speak("nothing buddy, whatsup")    

            elif query in ["how are you", "how about you"]:
                speak("i am good buddy")

            elif query in ["how's my outfit today", "how is my outfit today", "what do you think about my outfit"]:
                speak("its pretty nice buddy, you look so cool")
            
            elif query in ["who are you", "hey who are you"]:
                speak("i am, mark 42, you can ask me any help at any time, i will do for you buddy")

            elif  query in ["what's the weather today", "today's weather", "what about the climate today", "what about the weather today", "climate", "weather", "check the climate", "check the weather"]:
                speak("wait a moment buddy, i am checking")
                webbrowser.open("chennai weather")
                speak("according to today's weather")

            elif query in ["time please", "what's the time now", "tell me what's the time now"]:
                time_now()

            elif query in ["date please", "what's the date today", "tell me what's the date today"]:
                date_today()
            
            elif query in ["set a reminder", "set a reminder for me", "set an alarm"]:
                speak("yeah tell me")
                speak("when you want to remind")
                reminder()
            
            elif query in ["feeling sleepy", "are you feeling sleepy", "boring"]:
                speak("no buddy, i like to spend time with you")

            elif query in ["wikipedia", "open wikipedia"]:
                speak("what do you want from wikipedia buddy")
                search = command()
                speak("searching in wikipedia")
                results = wikipedia.summary(search, sentences=2)
                speak("according to wikipedia")
                speak(results)
        
            elif  query in ["youtube", "open youtube"]:
                speak("opening youtube")
                webbrowser.open("youtube.com")

            elif  query in ["mail", "gmail", "email", "open my mail", "check my mails", "check my mail"]:
                speak("opening gmail")    
                webbrowser.open("gmail.com")

            elif query in ["open google", "google", "browser", "open browser", "open search engine"]:
                speak("opening google")
                speak("what do you want to search in google")
                search = command().lower()
                webbrowser.open("https://google.com", new = 1)
                time.sleep(5)
                typewrite(search)
                press("enter")
                
            elif query in ["play some songs", "play any song", "play melody songs", "play any melody song", "relax my mind", "i have a headache", "song please"]:
                speak("playing songs, enjoy the song buddy")
                song_list = os.listdir("D:\\songs")
                os.startfile(os.path.join("D:\\songs", song_list[random.randint(0, len(song_list))]))
                
            elif query in ["close", "quit this", "please quit", "please close it", "close it", "just close"]:
                s = size()
                a = list(s)
                x = s[0] - 15
                moveTo(x, 0)
                click()
                
            elif query in ["play some videos", "play any video", "video please", "videos"]:
                speak("playing video, have fun buddy")
                video_list = os.listdir("E:\\videos")
                os.startfile(os.path.join("E:\\videos", video_list[random.randint(1, len(video_list))]))

            elif query in ["battery", "tell me how much energy you have", "how much energy you have", "your energy level", "energy level", "battery level"]:
                battery_percentage()
            
            elif query in ["camera", "open camera", "turn on camera"]:
                speak("opening camera")
                cam = cv2.VideoCapture(0)
                while True:
                    img = cam.read()[1]
                    cv2.imshow('camera',img)
                    k = cv2.waitKey(10)
                    if k == 27:
                        break
                cam.release()
                cv2.destroyAllWindows()

            elif query in ["show me the bluetooth devices", "tell me the bluetooth devices", "bluetooth devices", "check the bluetooth devices", "nearby bluetooth devices"]:
                speak("just a minute buddy, let me check")
                bluetooth_devices()

            elif query in ["scan him", "scan her", "find who he is", "find who she is", "who is this", "who he is", "who she is"]:
                os.startfile("E:\\Python\\AI\\sources\\Day - 7\\Face recognition.py")

            elif query in ["find a face", "search for face", "face detect on", "detect the face"]:
                os.startfile("E:\\Python\\AI\\sources\\Day - 5\\person face detector.py")

            elif query in ["i'll call you later buddy", "see you later", "bye", "see you", "call you later"]:
                speak("bye buddy ")
                speak("if you need anything you can call me at any time")
                speak("i will be there for you")
                exit()

        else:
            speak("sorry you are not my buddy, if you are my buddy tell me the password again otherwise, bye man, have a good day")
            pass
