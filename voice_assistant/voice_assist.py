#!/usr/bin/python3
"""voice assistant"""

import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    
def get_audio():
    pass

speak("Hello Jay")
