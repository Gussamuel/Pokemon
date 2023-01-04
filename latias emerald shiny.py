import time
import os
from pynput.keyboard import Key, Controller
import pyautogui
import PIL.ImageGrab
import imessage

keyboard = Controller()

def sendText():
    time.sleep(1)
    imessage.send(['+1 6155172055'], 'Shiny found!')
    time.sleep(1)
    imessage.send(['+1 6158303227'], 'Sam found a shiny and has no clue this text has been sent. Surprise him by replying with something funny!')
    time.sleep(1)
    imessage.send(['+1 6159745468'], 'Sam found a shiny and has no clue this text has been sent. Surprise him by replying with something funny!')
    time.sleep(1)
    imessage.send(['+1 6156360599'], 'Sam found a shiny and has no clue this text has been sent. Surprise him by replying with something funny!')

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

os.system("open /Applications/Operator.app")
time.sleep(1)

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
            

bigLoop()