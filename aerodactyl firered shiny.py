import time
import os
from pynput.keyboard import Key, Controller
import pyautogui
import PIL.ImageGrab
import imessage
import sys

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

def sendText():
    time.sleep(1)
    imessage.send(['+1 6155172055'], 'Shiny found!')

#THIS PROGRAM IS DESIGNED FOR FIRE RED
def shinyDetermined():
    #THIS FUNCTION DETERMINES IF THE POKEMON IS A SHINY BY CHECKING THE BORDER
    time.sleep(1.0)
    rgbShiny = 107, 227, 230, 255
    rgbShiny2 = 206, 170, 239, 255
    rgb = PIL.ImageGrab.grab().load()[1056,420]
    screen = PIL.ImageGrab.grab().size
    print(screen)
    print(rgb)
    time.sleep(1)
    if rgb == rgbShiny2:
        print(" {} resets.".format(get_var_value()))
        bigLoop()
    else:
        if rgb == rgbShiny:
            print(" {} resets.".format(get_var_value()))
            print("You got yourself a shiny!")
            print(" {} resets.".format(get_var_value()))
            sendText()
            exit()
        else:
            print(" {} resets.".format(get_var_value()))
            bigLoop()

def bigLoop():

    while True:
        count = 0
        #OPENS APPLICATION AND SOFT RESETS
        os.system("open /Applications/Operator.app")
        time.sleep(1)
        pyautogui.keyDown('return')
        pyautogui.keyDown('backspace')
        pyautogui.keyDown('x')
        pyautogui.keyDown('z')
        time.sleep(1)
        pyautogui.keyUp('return')
        pyautogui.keyUp('backspace')
        pyautogui.keyUp('x')
        pyautogui.keyUp('z')
        time.sleep(1)

        for i in range(8):
            keyboard.press('x')
            time.sleep(0.5)
            keyboard.release('x')
            time.sleep(0.5)
            count = count+1
            print(count, 'x')
            if count == 8:
                print('PHASE 1 DONE AT 8')

        for i in range(1):
            keyboard.press('z')
            time.sleep(1)
            keyboard.release('z')
            time.sleep(1)
            count = count+1
            print(count, 'z')
            if count == 9:
                print('PHASE 2 DONE AT 9')
#END OF TITLE SCREEN SEQUENCE

#PLAYER TALKS TO SCIENTIST
        for i in range(4):
            keyboard.press('x')
            time.sleep(0.4)
            keyboard.release('x')
            time.sleep(0.4)
            count = count+1
            print(count, 'x')
            if count == 13:
                print('PHASE 3 DONE AT 13')

        for i in range(4):
            keyboard.press('z')
            time.sleep(0.4)
            keyboard.release('z')
            time.sleep(0.4)
            count = count+1
            print(count, 'z')
            if count == 17:
                print('PHASE 4 DONE AT 17')
#PLAYER GOES TO THE MENU AND CHECKS THE POKEMON STARTING HERE
        for i in range(1):
            pyautogui.keyDown('return')
            time.sleep(0.5)
            pyautogui.keyUp('return')
            time.sleep(0.3)
            count = count+1
            print(count, 'return')
            if count == 18:
                print('PHASE 5 DONE AT 18')

        for i in range(1):
            pyautogui.keyDown('down')
            time.sleep(0.3)
            pyautogui.keyUp('down')
            time.sleep(0.3)
            count = count+1
            print(count, 'down')
            if count == 19:
                print('PHASE 6 DONE AT 19')

        for i in range(1):
            keyboard.press('x')
            time.sleep(0.4)
            keyboard.release('x')
            time.sleep(0.4)
            count = count+1
            print(count, 'x')
            if count == 20:
                print('PHASE 7 DONE AT 20')
        
        for i in range(2):
            time.sleep(0.5)
            pyautogui.keyDown('up')
            time.sleep(0.1)
            pyautogui.keyUp('up')
            time.sleep(0.3)
            count = count+1
            print(count, 'up')
            if count == 22:
                print('PHASE 8 DONE AT 22')

        for i in range(2):
            keyboard.press('x')
            time.sleep(0.3)
            keyboard.release('x')
            time.sleep(0.3)
            count = count+1
            print(count, 'x')
            if count == 24:
                print('PHASE 9 DONE AT 24')
                shinyDetermined()

bigLoop()