# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# Language in which you want to convert
language = 'en'

def speak(wordToSpeak):
    myobj = gTTS(text=wordToSpeak, lang=language, slow=False)
    myobj.save("wordToSpeak.mp3")
    os.system("afplay wordToSpeak.mp3")

wordToSpeak = "Enter first number: "
speak(wordToSpeak)
number1 = input(wordToSpeak)

wordToSpeak = "Enter second number: "
speak(wordToSpeak)
number2 = input(wordToSpeak)

#engine.say("Hmm. You want me to substract " + str(number2) + " from " + str(number1))
wordToSpeak = "Chia. You want me to substract " + str(number2) + " from " + str(number1)
speak(wordToSpeak)

result = number1 - number2

wordToSpeak = "Chia Rawat result of substraction between " + str(number1) + " and " + str(number2) + " is " + str(result)
print(wordToSpeak)
speak(wordToSpeak)
