import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import pyjokes
import datetime
import pyautogui as py

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
 
def processCommand(c):
    # will open websites
    if f"open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")  
    elif ("open twitter") in c.lower(): 
        webbrowser.open("https://twitter.com") 
    elif ("open chatgpt") in c.lower(): 
        webbrowser.open("https://chatgpt.com")
    # play the songs in the song library 
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        if song in musicLibrary.music:
            link=musicLibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
             speak(f"Sorry, I couldn't find the song {song} in the library.")
    # basic conversations
    elif "deactivate" in c.lower():
        speak("ok sir. you can call me anytime. bye")
        exit()
    elif "hello" in c.lower():
         speak("hello sir, how are you")
    elif "how are you" in c.lower():
         speak("i am perfect sir")
    elif c.lower()=="thank you" :
         speak("i am grateful to serve you")
    elif "tell me a joke" in c.lower():
         speak(pyjokes.get_joke())
    elif "time" in c.lower():
         strTime=datetime.datetime.now().strftime("%H:%M")
         speak(f"sir, the time is {strTime}")
    elif "screenshot" in c.lower():
         py.screenshot("screenshot.png")
         speak("screenshot taken.")
    # unhandalable command
    else:
        speak("I am sorry, i am not capable to handle that command")

if __name__=="__main__":
   speak("Initializing Jarvis....") 
   while True:
        # Listen for the wake word "Jarvis"
        # Obtain audio from the microphone
        r = sr.Recognizer()
        print("Listening")
        try:
            with sr.Microphone() as source:
                r.pause_threshold=1
                audio = r.listen(source)
            word=r.recognize_google(audio)
            if("jarvis" in word.lower()):
                speak("Yes sir, how can i help you")
                # listen for command
                with sr.Microphone() as source:
                    r.pause_threshold=1
                    audio = r.listen(source)
                    command=r.recognize_google(audio, language="en-in")   
                    # process the command
                    processCommand(command)
        except Exception as e:
            print(f"An error occurred: {e}")
                        