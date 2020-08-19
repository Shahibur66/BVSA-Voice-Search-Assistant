from gtts import gTTS
import os
import playsound

''' converting text to speech using gTTS '''
def textToSpeech():
    tts = gTTS(text="Voice search assistant could not recognize your speech, try again. ", lang='en')
    tts.save("assets\\audio\\initVoice.mp3")

    
''' playing initVoice.mp3 using playsound'''
def playSpeech():
    playsound.playsound("assets\\audio\\initVoice.mp3", True)
    
##textToSpeech()
##playSpeech()
