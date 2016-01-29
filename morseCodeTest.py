#!/usr/bin/python
from random import randint

rules = """
This is a morse to english and english to morse testing app
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

    print ('\nWhat is the {0} for {1}'.format(unicode(code, 'utf-8'), unicode(q, 'utf-8'))) 
    answer = raw_input("Enter answer or q to quit or h for help \nYour answer: ")

    if(answer == 'q'):
      play = 0
    elif(answer == 'h'):
      print '\n=============================================================================================='
      print rules
      print '=============================================================================================='
      for index in range(65, 91):
        letter = chr(index)
        morseCode = englishChars[letter]
        if(((index-64) % 3) == 0):
          print (letter + ' = ' + morseCode)
        else:
          space = (' ' * (10 - len(morseCode)))
          print (letter + ' = ' + morseCode + space),
      print '\n=============================================================================================='

    elif(answer == a or answer.upper() == a):
      print ("\nYes {0} is the correct answer!".format(unicode(a, 'utf-8')))
    else:
      print ("\nNo {0} is not the correct answer \n{1} is the correst answer".format(unicode(answer, 'utf-8'), unicode(a, 'utf-8')))
