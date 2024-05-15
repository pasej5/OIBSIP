import speech_recognition as sr
import webbrowser
import time

def get_audio(prompt=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if prompt:
            print(prompt)
        else:
            print('Dont be shy say something')
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
    voice_data = voice_data.lower()
    if "hello" in voice_data:
        print("Hello! How can I assist you today")
    elif "what is your name" in voice_data:
        print("My name is Matsika")
    elif "what time is it" in voice_data:
        print(f"The current time is {time.strftime('%I:%M %p')}")
    elif "search" in voice_data:
        search_query = get_audio("What would you like to search for?")
        if search_query:
            url = 'https://google.com/search?q=' + search_query
            
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe' 
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open(url)
            print(f"This is what i found for '{search_query}'")
        
    else:
        print("I'm not sure how to respond to that.")

if __name__ == "__main__":
    voice_data = get_audio()
    respond(voice_data)
