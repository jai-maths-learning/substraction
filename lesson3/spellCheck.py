# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Hello Jai Rawat hello Chia !'

# Language in which you want to convert
language = 'en'

def speak(wordToSpeak):
    myobj = gTTS(text=wordToSpeak, lang=language, slow=False)
    myobj.save("wordToSpeak.mp3")
    os.system("afplay wordToSpeak.mp3")


with open("wordlist.txt") as f:
    fileLines = f.readlines()

score=0
totalScore=0
for word in fileLines:
    wordToSpeak = "Jai What is spelling of " + word
    speak(wordToSpeak)
    wordSpelling = raw_input("Spelling?: ")
    #print(word)
    #print(wordSpelling)
    if word == wordSpelling+"\n":
        score=score+1
    totalScore = totalScore + 1


print("Your total score is " + str(score) + " out of " + str(totalScore))
