import speech_recognition as sr
import webbrowser
import time

def get_audio(ask = False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('How can I help you today?')
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ""
        
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
        except sr.RequestError:
            print("Sorry, I'm unable to process that request right now.")
            
        return voice_data

def respond(voice_data):
    if "what is your name" in voice_data.lower():
        print("My name is Matsika")
    elif "what time is it" in voice_data.lower():
        print(f"The current time is {time.strftime('%I:%M %p')}")
    elif "search" in voice_data:
        search = get_audio("what are we serching today")
        url = 'https://google.com/search?q=' + search 
        webbrowser.get().open(url)
        print("This is what i found for") + search
        
    else:
        print("I'm not sure how to respond to that.")

voice_data = get_audio()
respond(voice_data)
