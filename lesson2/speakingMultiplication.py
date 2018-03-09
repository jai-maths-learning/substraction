# Import the required module for text
# to speech conversion
from gtts import gTTS
from random import *

# This module is imported so that we can
# play the converted audio
import os

# Language in which you want to convert
language = 'en'

def speak(wordToSpeak):
    myobj = gTTS(text=wordToSpeak, lang=language, slow=False)
    myobj.save("wordToSpeak.mp3")
    os.system("afplay wordToSpeak.mp3")

mytext="yes"
while mytext == "yes":

    number1 = randint(1, 17)
    number2 = randint(1, 10)

    #engine.say("Hmm. You want me to substract " + str(number2) + " from " + str(number1))


    result = number1 * number2
    wordToSpeak = "Jai Chia What is multiplication of " + str(number1) + " and " + str(number2)
    speak(wordToSpeak)


    mytext = raw_input("Do you want to continue?")
    wordToSpeak = "Do you want to continue "
    speak(wordToSpeak)


    wordToSpeak = "Chia multiplication of " + str(number1) + " and " + str(number2) +  " is "  + str(result)
    speak(wordToSpeak)
