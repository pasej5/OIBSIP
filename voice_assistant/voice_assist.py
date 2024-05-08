from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    sound = AudioSegment.from_file(filename, format="mp3")
    play(sound)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        
        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception: " + str(e))
            
    return said

# text_to_speak = "Hello, this is your voice assistant speaking."
# speak("hello")
# print(get_audio())

text = get_audio()

if "hello" in text:
    speak("hello, you are blessed")
    
if "what is your name" in text:
    speak("My name is Matsika")
