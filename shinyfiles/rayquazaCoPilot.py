#the goal of this program is to soft reset pokemon Sapphire within the Operator app until a shiny is found
#the way this should be done is by using OpenCV to compare screenshots of the game to a screenshot of a shiny pokemon in the "project3" folder
#do NOT use PIL to compare screenshots, ONLY use PIL to take screenshots
#the program should only stop once a shiny is found
#when a shiny is found the program should send a text message to my phone

import os
import time
import pyautogui
import PIL
import cv2
import numpy as np
import imessage
import sys
from pynput.keyboard import Key, Controller
from PIL import Image
from PIL import ImageGrab

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

def shinyDetermined():
    #THIS FUNCTION DETERMINES IF THE POKEMON IS A SHINY BY CHECKING THE BORDER
    time.sleep(0.5)
    rgbShiny2 = 255, 219, 0, 255
    rgb = PIL.ImageGrab.grab().load()[600,460]
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
        for i in range(4):
            time.sleep(0.5)
            keyboard.press('x')
            time.sleep(0.4)
            keyboard.release('x')
            time.sleep(0.4)
            count = count+1
            print(count, 'x')
            time.sleep(0.5)
        time.sleep(1)
        #GETS A SCREENSHOT OF THE GAME
        im = PIL.ImageGrab.grab(bbox=(0, 0, 2404, 1578))
        im.save('screenshot.png')
        #OPENS THE SCREENSHOT AND CONVERTS IT TO GRAYSCALE
        img = cv2.imread('screenshot.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #COMPARES THE SCREENSHOT TO THE SHINY POKEMON IMAGE AND PRINTS THE RESULT
        template = cv2.imread('shiny.png',0)
        res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        if len(loc[0]) > 0:
            print(" {} resets.".format(get_var_value()))
            print("You got yourself a shiny!")
            print(" {} resets.".format(get_var_value()))
            print(" {} shiny pokemon.".format(get_var_valueShiny()))
            sendText()
            exit()
        else:
            print(" {} resets.".format(get_var_value()))
            print('Not a shiny.')
            bigLoop()

bigLoop()