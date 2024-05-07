from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    sound = AudioSegment.from_file(filename, format="mp3")
    play(sound)

text_to_speak = "Hello, this is your voice assistant speaking."
speak(text_to_speak)
