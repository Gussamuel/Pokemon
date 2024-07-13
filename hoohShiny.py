import time
import os
from pynput.keyboard import Key, Controller
import pyautogui
from PIL import Image, ImageDraw, ImageGrab
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
        
        # Check if the reset count is a multiple of 20
        if val % 100 == 0:
            sendText(val)  # Send a text message
            
        return val

def sendText(reset_count):
    imessage.send(['+1 6155172055'], f'Hunt ongoing...reset count: {reset_count}')

def shinyText(reset_count):
    imessage.send(['+1 6155172055'], f'Shiny found! Reset count: {reset_count}')

def shinyDetermined():
    rgbShiny2 = (66, 210, 82, 255)
    
    # Take a screenshot
    screenshot = ImageGrab.grab()
    
    # Coordinates to check
    x, y = 1686, 364  # Update these coordinates if necessary
    
    # Get the pixel value at the specified coordinates
    rgb = screenshot.load()[x, y]
    
    # Print the screen size and the captured RGB value
    screen = screenshot.size
    print("Screen size:", screen)
    print("Captured RGB value at ({}, {}): {}".format(x, y, rgb))
    print("\n")
 
    if rgb == rgbShiny2:  # Compare only the RGB values, ignoring alpha
        print(" {} resets.".format(get_var_value()))
        print("\n")
        print('Not a shiny.')
        bigLoop()
    else:
        print(" {} resets.".format(get_var_value()))
        print("\n")
        print("You got yourself a shiny!")
        print(" {} resets.".format(get_var_value()))
        print(" {} shiny pokemon.".format(get_var_value()))
        shinyText(get_var_value())  # Send shiny found text with current reset count
        exit()

def bigLoop():
    while True:
        count = 0
        os.system("open /Applications/Playback.app")
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

        for i in range(6):
            keyboard.press('x')
            time.sleep(0.5)
            keyboard.release('x')
            time.sleep(0.5)
            count = count + 1
            print(count, 'x')
            if count == 6:
                print('PHASE 1 DONE AT 6')

        for i in range(1):
            keyboard.press('z')
            time.sleep(1)
            keyboard.release('z')
            time.sleep(1)
            count = count + 1
            print(count, 'z')
            if count == 7:
                print('PHASE 2 DONE AT 7')

        for i in range(2):
            time.sleep(0.5)
            pyautogui.keyDown('up')
            time.sleep(0.4)
            pyautogui.keyUp('up')
            time.sleep(0.4)
            count = count + 1
            print(count, 'up')
            if count == 10:
                print('PHASE 3 DONE AT 9')

        time.sleep(3.5)
        print("Calling shiny determined...")
        shinyDetermined()

bigLoop()