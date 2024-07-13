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
    
keyboard = Controller()

os.system("open /Applications/Playback.app")
time.sleep(1)

def sendText():
    time.sleep(1)
    imessage.send(['+1 6155172055'], 'Shiny found!')

def shinyDetermined():
    keyboard.press('x')
    time.sleep(3.5)
    rgbShiny = 255, 105, 107, 255
    rgb = PIL.ImageGrab.grab().load()[1600,640]
    screen = PIL.ImageGrab.grab().size
    print(rgb)
    if rgb == rgbShiny:
        time.sleep(0.3)
        pyautogui.keyDown('right')
        time.sleep(0.3)
        pyautogui.keyUp('right')
        time.sleep(0.3)
        pyautogui.keyDown('down')
        time.sleep(0.3)
        pyautogui.keyUp('down')
        time.sleep(0.5)
        for i in range(3):
            keyboard.press('x')
            time.sleep(0.5)
            keyboard.release('x')
            time.sleep(1)
        for i in range(4):
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(1)
        bigLoop()
    else:
        print('You got yourself a shiny!')
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
        
        
        
bigLoop()






def bigLoop():

    callFound = 107, 235, 181, 255

    pyautogui.keyDown('down')
    time.sleep(3)
    pyautogui.keyUp('down')
    
    pyautogui.keyDown('up')
    time.sleep(3)
    pyautogui.keyUp('up')
    while True:
        call = PIL.ImageGrab.grab().load()[1108,1144]
        if callFound == call:
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            keyboard.press('z')
            time.sleep(0.5)
            keyboard.release('z')
            time.sleep(0.5)
            bigLoop()
        else:
            break
    
    keyboard.press('x')
    time.sleep(0.5)
    keyboard.release('x')
    keyboard.press('x')
    time.sleep(0.5)
    keyboard.release('x')
    keyboard.press('x')
    time.sleep(0.5)
    keyboard.release('x')
    time.sleep(14)
    shinyDetermined()
            