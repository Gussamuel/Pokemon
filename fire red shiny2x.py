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
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val

def get_var_valueShiny(filename="varstoreShiny.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val

def get_var_valueError(filename="varstoreError.dat"):
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

#THIS PROGRAM IS DESIGNED FOR FIRE RED
def shinyDetermined():
    #THIS FUNCTION DETERMINES IF THE POKEMON IS A SHINY BY CHECKING THE BORDER
    time.sleep(1.5)
    rgbShiny = 107, 227, 230, 255
    rgbShiny2 = 206, 170, 239, 255
    rgb = PIL.ImageGrab.grab().load()[1056,420]
    screen = PIL.ImageGrab.grab().size
    print(screen)
    print(rgb)
    time.sleep(1)
    if rgb == rgbShiny2:
        print(" {} resets.".format(get_var_value()))
        print('Not a shiny.')
        bigLoop()
    else:
        if rgb == rgbShiny:
            print(" {} resets.".format(get_var_value()))
            print("You got yourself a shiny!")
            print(" {} resets.".format(get_var_value()))
            print(" {} shint pokemon.".format(get_var_valueShiny()))
            sendText()
            exit()
        else:
            print(" {} resets.".format(get_var_value()))
            print('Something weird happened here and I could not scan the border. It was not visible.')
            print(" {} errors.".format(get_var_valueError()))
            bigLoop()

def bigLoop():

    while True:
        count = 0
        #OPENS APPLICATION AND SOFT RESETS
        os.system("open /Applications/Operator.app")
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

        for i in range(7):
            keyboard.press('x')
            time.sleep(0.4)
            keyboard.release('x')
            time.sleep(0.4)
            count = count+1
            print(count, 'x')
            

        for i in range(1):
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            count = count+1
            print(count, 'z')

#END OF TITLE SCREEN SEQUENCE

#PLAYER TALKS TO SCIENTIST
        sleep(randint(1,10))

        for i in range(4):
            keyboard.press('x')
            time.sleep(0.2)
            keyboard.release('x')
            time.sleep(0.2)
            count = count+1
            print(count, 'x')

        for i in range(3):
            keyboard.press('z')
            time.sleep(0.4)
            keyboard.release('z')
            time.sleep(0.4)
            count = count+1
            print(count, 'z')

#PLAYER GOES TO THE MENU AND CHECKS THE POKEMON STARTING HERE
        for i in range(1):
            pyautogui.keyDown('return')
            time.sleep(0.5)
            pyautogui.keyUp('return')
            time.sleep(0.3)
            count = count+1
            print(count, 'return')

        for i in range(1):
            pyautogui.keyDown('down')
            time.sleep(0.3)
            pyautogui.keyUp('down')
            time.sleep(0.3)
            count = count+1
            print(count, 'down')

        for i in range(1):
            keyboard.press('x')
            time.sleep(0.4)
            keyboard.release('x')
            time.sleep(0.4)
            count = count+1
            print(count, 'x')
        
        for i in range(2):
            time.sleep(0.3)
            pyautogui.keyDown('up')
            time.sleep(0.1)
            pyautogui.keyUp('up')
            time.sleep(0.3)
            count = count+1
            print(count, 'up')

        for i in range(2):
            keyboard.press('x')
            time.sleep(0.3)
            keyboard.release('x')
            time.sleep(0.3)
            count = count+1
            print(count, 'x')

        shinyDetermined()

bigLoop()