import pyttsx3   #pyttsx3 is a python library used for text-speech conversion  .It works offline also
#pip install pyttsx3
import datetime
import speech_recognition as sr
# pip install speechRecognition  
#in takecommand() functn
import pyaudio
#pip install wikipedia
import wikipedia
import webbrowser
import os
import random
import smtplib
from datetime import date

engine=pyttsx3.init("sapi5") 
#sapi5 is a speech synthesis engine developed by Microsoft ,It  gives access to installed text-speech recognition voices on Windows system
#"sapi5" (Speech Application Program Interface ) it is an Interface used to convert sppeech-text and vice versa
voices=engine.getProperty("voices")
# print(voices)# it print two voices male&female
# print(voices[0].id) # It will print one voice i,e male(0)  for female we have to use "1"
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak(" I am Alexa sir, How can I help you?")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1 #seconds of non-speaking audio before a phrse is considered complete 
        audio = r.listen(source)
    try:
        print("Recognizing.........")
        query=r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n ")
    except Exception as e:
        # print(e)
        print("Please, say that again...")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com", 387)
    server.ehlo()
    server.startls()
    server.login("divyakandhakula2003@gmail.com","Divyak@19")
    server.sendmail("divyakandhakula2003@gmail.com",to,content)
    server.close()

if __name__=="__main__":
    # speak("Welcome, how may i help you")
    wishme()
    if 1:
        query=takecommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia......")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia......")
            print(results)
            speak(results)
        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            
        elif "play music" in query:
            music_directory="C:\\Users\\divya\Music\\music_directory"
            songs=os.listdir(music_directory)
            random_song=random.choice(songs)
            os.startfile(os.path.join(music_directory, random_song)) #here at random_music if we give "songs[2]" it will play thesecond song in the list

        elif "the time" in query:
            Stime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is : {Stime}")
        
        elif "open code" in query:
            code="C:\\Users\\divya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
            os.startfile(code)
        
        elif "name " in query:
            speak("My name is Alexa")
            # d=takecommand()
            # if "change name" in d:
            #     n=takecommand()
            #     name="Alexa"
            #     name=name.replace("Alexa",n)
            #     speak(f"My name is {name}")
        elif "send email" in query:
            try:
                speak("What should I say?")
                content=takecommand()
                to="shruthikandukula@gmail.com"
                sendEmail(to,content)
                speak("Your email has been sent")
            except Exception as e:
                speak("Sorry! Email  not sent")
        elif "date" in query:
            tdate=date.today()
            speak(f"today's date is:{tdate}")
        
