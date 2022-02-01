#!/usr/bin/env python3
#Phyton Morseprogramm fuer Status LED
#12.05.2021
#Karoline Hrastnig
from gpiozero import LED
from time import sleep
from signal import pause

STATUS_LED=25



TDOT=0.2



#Dictionary (Hash Array  // analog zu assoziatieves Array in php)
code = {"0" :"-----",
        "1" : ".----",
        "2" : "..---",
        "3" :"...--",
        "4" : "....-",
        "5" : ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--.."}

#for zahl, morse in code.items()
# print("Zahl: " + zahl)
# print("Morsecode: " + morse)
# print(code[1])
x = LED(STATUS_LED)

def morse(zeichen, led):
    if zeichen not in code:
        print("Nicht vorhanden")
        return
    print(code[z])
    for n in code[z]:
        if n=="-":
            x.blink(3*TDOT,TDOT,1,False)
            print("-")
        else:
            x.blink(TDOT,TDOT,1,False)
            print(".")
    
    
while True:
    nachricht = input("zahl oder buchstabe: ").upper() #input um etwas auszugeben, .upper() um Kleinbuchstaben als Grossbuchstaben auszugeben.
    if nachricht == "#":
        print("Bye")
        break
    for z in nachricht:
        print(z)
        morse(z, x)
        sleep(2*TDOT)
#Ene Andere Möglichkeit der Wahrheitsabfrage:
#while True:
#    try:
#       nachricht = input("zahl oder buchstabe: ").upper() 
#       blink(code[zeichen])
#    except KeyError as err:
#       print("Nicht im Code enthalten: ", err.args[0])  // Fehermeldung solte sinnvoll sein
#    except KeyboardInterupt:
#       print("Bye")
#       sys.exit()
