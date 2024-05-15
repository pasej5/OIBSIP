import speech_recognition as sr
import webbrowser
import time
from gtts import gTTS
import os
import random
from pydub import AudioSegment
from pydub.playback import play

def get_audio(prompt=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if prompt:
            speak(prompt)
        else:
            print('Dont be shy say something')
        audio = r.listen(source)
        voice_data = ""

        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
        except sr.RequestError:
            speak("Sorry, I'm unable to process that request right now.")

        return voice_data

def speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    sound = AudioSegment.from_file(audio_file, format="mp3")
    play(sound)
    os.remove(audio_file)

def respond(voice_data):
    voice_data = voice_data.lower()
    if "hello" in voice_data:
        speak("Hello! How can I assist you today")
    elif "what is your name" in voice_data:
        speak("My name is Matsika")
    elif "what time is it" in voice_data:
        speak(f"The current time is {time.strftime('%I:%M %p')}")
    elif "search" in voice_data:
        search_query = get_audio("What would you like to search for?")
        if search_query:
            chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            url = 'https://google.com/search?q=' + search_query
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open(url)
            speak(f"This is what i found for '{search_query} '")
    elif "find location" in voice_data:
        location = get_audio("What is the location?")
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open(url)
        speak("This is what i found for " + location)
    elif "exit" in voice_data:
        exit()
    else:
        speak("I'm not sure how to respond to that.")

time.sleep(1)
speak("Hello! How can I assist you today")

while True:
    voice_data = get_audio()
    respond(voice_data)
