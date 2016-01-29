#!/usr/bin/python
from random import randint

"""
this is a morse to english and english to morse testing app
to improve understanding of morse code

Morse Code Rules:
1. The length of a dot is one unit.
2. A dash is three units.
3. The space between parts of the same letter is one unit.
4. The space between letters is three units.
5. The space between words is seven units.

"""

englishChars = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-','R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}

morseChars = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}


def getMorse(letter):
  return englishChars[letter.upper()]

def getEnglish(morse):
  return morseChars[morse];

if __name__ == '__main__':
  play = 1

  while(play):
    coin = randint(0,1)
    randLetter = chr(randint(0, 25) + 65) #65 is the ascii for 'A'
    a = randLetter
    q = getMorse(randLetter)
    code = "English letter"
    if(not coin):
      code = "Morse Code"
      a = q
      q = getEnglish(q)

    # print (a, q)
    print ('What is the {0} for {1}'.format(unicode(code, 'utf-8'), unicode(q, 'utf-8'))) 
    answer = raw_input("Your answer: ")

    if(answer == a):
      print ("Yes {0} is the correct answer!".format(unicode(a, 'utf-8')))
    else:
      print ("No {0} is not the correct answer \n{1} is the correst answer".format(unicode(answer, 'utf-8'), unicode(a, 'utf-8')))

    keepPlaying = raw_input("Continue playing (yes / no): ")
    play = (keepPlaying == 'yes') and 1 or 0