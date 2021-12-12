import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 4:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I am Cadet, Please tell me how can i help you")


def takeCommand():
    # it takes input from microphone and gives output in the form of string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please.")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('1907867@ggi.ac.in', 'your pwd')
    server.sendmail('1907867@ggi.ac.in', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # executing task as per query
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia...")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open github' in query:
            webbrowser.open("github.com/Bandhan-singh-katoch")

        elif 'play music' in query:
            music_dir = 'G:\\YMusic'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[5]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open chrome' in query:
            appPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(appPath)

        elif 'email to boss' in query:
            try:
                speak("What should i send to bandhan boss ?")
                content = takeCommand()
                to = "parbhatbandhan@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send the mail")
