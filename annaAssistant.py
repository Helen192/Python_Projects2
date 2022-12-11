import pyttsx3
import datetime  # help anna to get the time
import speech_recognition as sr
import webbrowser as wb  # this library allows to search web automatically
import os



anna = pyttsx3.init()  # object anna
voice = anna.getProperty('voices')   # take existing voice of library
anna.setProperty('voice', voice[1].id) # choose type of voice. Here is voice of woman

def speak(audio):
    print('Anna:', audio)
    anna.say(audio)
    anna.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Sir")
    elif hour >= 18 and hour < 23:
        speak("Good evening Sir")
    else:
        speak("Good night Sir")
    speak("How can I help you?")

def command():
    record_voice = sr.Recognizer()  # this object is to get the verbal command
    with sr.Microphone() as source:  # declare, where is the verbal command come from
        record_voice.pause_threshold = 2 # the pause time before hearing a new command
        audio = record_voice.listen(source)
    try:
        query = record_voice.recognize_google(audio, language='en')
        print("Helen: " + query)
    except sr.UnknownValueError:
        print("Please repeat or type the command")
        query = input("Your command is: ")
    return query

if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()  # hearing command from users
        if "google" in query:
            speak("What should I search boss?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on google")
        elif "youtube" in query:
            speak("What should I search boss?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        elif "time" in query:
            time()
        elif "open video" in query:
            yoga = r"C:\Users\dream\Desktop\testvideo\yoga.mp4"
            os.startfile(yoga)  # run file yoga
        elif "quit" in query:
            speak("Anna is quitting sir. Goodbye boss")
            quit()