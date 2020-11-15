import time
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()

voices = engine.getProperty('voices') 

# to check the voices available in the system
'''for voice in voices: 
	print("Voice:") 
	print("ID: %s" %voice.id) 
	print("Name: %s" %voice.name) 
	print("Age: %s" %voice.age) 
	print("Gender: %s" %voice.gender) 
	print("Languages Known: %s" %voice.languages) '''

# female
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
engine.say("Hello, I am Zira.")
engine.runAndWait()

# male
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
engine.say("Hello,I am David.")
engine.runAndWait()

# Voice menu
while(1):
    engine.say("Choose the language you want to speak in")
    engine.runAndWait()
    time.sleep(0.2)
    print("1. English")
    engine.say("1. English")
    engine.runAndWait()
    time.sleep(0.2)
    print("2. Hindi")
    engine.say("2. Hindi")
    engine.runAndWait()
    time.sleep(0.2)
    print("3. Kannada")
    engine.say("3. Kannada")
    engine.runAndWait()
    time.sleep(0.2)
    print("4. Bengali")
    engine.say("4. Bengali")
    engine.runAndWait()
    time.sleep(0.2)
    print("5. Malayalam")
    engine.say("5. Malayalam")
    engine.runAndWait()
    time.sleep(0.2)
    print("6. Marathi")
    engine.say("6. Marathi")
    engine.runAndWait()
    time.sleep(0.2)
    print("7. Urdu")
    engine.say("7. Urdu")
    engine.runAndWait()
    time.sleep(0.2)
    print("8. Others")
    engine.say("8. Others")
    engine.runAndWait()
    time.sleep(0.2)
    n = int(input("\nEnter your choice:"))
    lang = 'en'
    if n == 1:
        lang = 'en'
    elif n == 2:
        lang = 'hi-IN'
    elif n == 3:
        lang = 'kn-IN'
    elif n == 4:
        lang = 'bn-IN'
    elif n == 5:
        lang = 'ml-IN'
    elif n == 6:
        lang = 'mr-IN'
    elif n == 7:
        lang = 'ur'
    elif n == 8:
        lang = input("Enter the google language code of the language you want to see the output in: ")
    elif n == 0:
        exit(0)
    with sr.Microphone() as source:
        engine.say("Mic testing..")
        engine.runAndWait()
        audio = r.adjust_for_ambient_noise(source)
        print("Say something")
        audio = r.listen(source)
        engine.say("Time is over. Thanks.")
        engine.runAndWait()
    try:
        print("You said: ' " + r.recognize_google(audio, language=lang) + "'")   
        time.sleep(5)
    except LookupError:
        engine.say("Could not understand audio. Do you want to try again?")
        engine.runAndWait()
    engine.say("Do you want to continue?")
    engine.runAndWait()
    y = int(input("Enter 0 to quit"))
    if y == 0:
        exit(0)

engine.runAndWait()