import re
import speech_recognition
import playsound
import googleSearch
import sys
import threading
errors=[]

''' function which recognize speech using speech recognition and re modules. '''

def speechRecognition(lang,min_value,max_value,sleep_time):
    
    recognizer=speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        #print("Listening...")

        audio=recognizer.listen(source)
        words=""
    try:
        ban=1
        if lang is ban:
            words=recognizer.recognize_google(audio,language="bn-BD")
        else:
            words=recognizer.recognize_google(audio)
            
        matches=re.search("Hey bot search for me (.*)",words)
        googleSearch.googleSearch(words,matches,min_value,max_value,sleep_time)
    except:
        errors.append('Voice search assistant could not recognize your speech, try again.')
        errors.append(" ")
        errors.append("Turn ON, to search your queries.")
        errors.append(" ")
        
    print('Done from speechRecognition')


def getRecognitionErrors():
    return errors 

def closeRec():
    sys.exit(0)


