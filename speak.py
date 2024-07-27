#! text to speech :
import pyttsx3
def speak(text):
    engine  = pyttsx3.init()
    id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
    engine.setProperty('voice',id)
    engine.say(text=text)
    engine.runAndWait()
speak("hello")