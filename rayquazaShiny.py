import time
from time import sleep
import os
from pynput.keyboard import Key, Controller
import pyautogui
import PIL.ImageGrab
import imessage
import sys
from random import randint

sys.setrecursionlimit(6000)

keyboard = Controller()

def get_var_value(filename="varstore.dat"):
    #THIS FUNCTION STORES THE NUMBER OF RESETS
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val

def get_var_valueShiny(filename="varstoreShiny.dat"):
    #THIS FUNCTION STORES THE NUMBER OF SHINY POKEMON
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val

def sendText():
    time.sleep(1)
    imessage.send(['+1 6155172055'], 'Shiny found!')

#THIS PROGRAM IS DESIGNED FOR EMERALD
def shinyDetermined():
    #THIS FUNCTION DETERMINES IF THE POKEMON IS A SHINY BY CHECKING THE BORDER
    time.sleep(0.5)
    rgbShiny2 = 90, 186, 140, 255
    rgb = PIL.ImageGrab.grab().load()[1440,400]
    screen = PIL.ImageGrab.grab().size
    print(screen)
    print(rgb)
    time.sleep(1)
    if rgb == rgbShiny2:
        print(" {} resets.".format(get_var_value()))
        print('Not a shiny.')
        bigLoop()
    else:
        print(" {} resets.".format(get_var_value()))
        print("You got yourself a shiny!")
        print(" {} resets.".format(get_var_value()))
        print(" {} shiny pokemon.".format(get_var_valueShiny()))
        sendText()
        exit()

def bigLoop():

    while True:
        count = 0
        #OPENS APPLICATION AND SOFT RESETS
        os.system("open /Applications/Playback.app")
        time.sleep(0.5)
        pyautogui.keyDown('return')
        pyautogui.keyDown('backspace')
        pyautogui.keyDown('x')
        pyautogui.keyDown('z')
        time.sleep(0.5)
        pyautogui.keyUp('return')
        pyautogui.keyUp('backspace')
        pyautogui.keyUp('x')
        pyautogui.keyUp('z')
        time.sleep(0.5)

        for i in range(6):
            time.sleep(0.5)
            keyboard.press('x')
            time.sleep(0.4)
            keyboard.release('x')
            time.sleep(0.4)
            count = count+1
            print(count, 'x')

        shinyDetermined()

bigLoop()