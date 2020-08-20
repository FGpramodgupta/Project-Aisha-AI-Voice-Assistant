#import speech_recognition as s_r
#print(s_r.__version__) # just to print the version not required
#r = s_r.Recognizer()
#my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
#with my_mic as source:
#    print("Say now!!!!")
#    audio = r.listen(source) #take voice input from the microphone
#print(r.recognize_google(audio)) #to print voice into text


# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:11:16 2019

@author: Pramod Gupta
"""


import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pandas as pd
import random

jokedatabase=pd.read_csv('shortjokes.csv')
jokedatabase=jokedatabase[['Joke']]
#print(len(jokedatabase))


thankyouresponse=[ 'You’re welcome.','No problem.','No worries.','Don’t mention it.','My pleasure.','Anytime.','It was the least I could do.','Glad to help.','Sure!']

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Sneha. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
#        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit = 5)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
#        speak('Say that again please...')
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pramodgupta498@gmail.com', '9223206598')
    server.sendmail('pramodgupta498@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        print(query)
#        if query == 0: 
#            print('Waiting')
#            continue


        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'thanks' in query or 'thank' in query:
            speak(random.choice(thankyouresponse))
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Here you go")
            
        elif 'open google' in query:
            speak("Here you go")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
            speak("Here you go")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
#            speak("Here you go")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("Here you go, it will take sometime to open")
            codePath = "C:\\Users\\1121113\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open r studio' in query:
            speak("Here you go, it will take sometime to open")
            codePath = "C:\\Program Files\\RStudio\\bin\\rstudio.exe"
            os.startfile(codePath)
            
        elif 'open anaconda' in query:
            speak("Here you go, it will take sometime to open")
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\Anaconda Navigator (Anaconda3).lnk"
            os.startfile(codePath)

        elif 'open Jupyter notebook' in query:
            speak("Here you go, it will take sometime to open")
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Jupyter Notebook (Anaconda3).lnk"
            os.startfile(codePath)

        elif 'open powershell prompt' in query:
            speak("Here you go, it will take sometime to open")
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Powershell Prompt (Anaconda3).lnk"
            os.startfile(codePath)
            
        elif 'open spyder' in query:
            speak("Here you go, it will take sometime to open")
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Spyder (Anaconda3).lnk"
            os.startfile(codePath)
            
        elif 'email to Pramod' in query or 'mail to Pramod' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pramod@mail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    

        elif 'sneha' in query:
            speak('Hello My name is Aisha, how can i help you')
#            wishMe()
            
#            speak("hello, What can i do for you?")
        elif 'joke' in query:


#            jokelist=['A doctor accidentally prescribes his patient a laxative instead of a coughing syrup. - Three days later the patient comes for a check-up and the doctor asks: "Well? Are you still coughing?"-The patient replies: "No. Im afraid to."'] 
#            print(len(jokedatabase))
            speak('')
            speak(str(jokedatabase.sample()))
            