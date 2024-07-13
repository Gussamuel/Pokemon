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
        return val

def get_var_valueShiny(filename="varstoreShiny.dat"):
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
    time.sleep(0.5)
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
    
    # Draw a marker on the image to indicate the pixel being checked
    # draw = ImageDraw.Draw(screenshot)
    # marker_size = 5
    # draw.rectangle([x-marker_size, y-marker_size, x+marker_size, y+marker_size], outline="red", width=3)
    
    # Save the screenshot to a file to visually inspect it
    # screenshot.save("screenshot_with_marker.png")
    
    time.sleep(1)
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
        print(" {} shiny pokemon.".format(get_var_valueShiny()))
        sendText()
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

        for i in range(3):
            time.sleep(0.5)
            pyautogui.keyDown('up')
            time.sleep(0.4)
            pyautogui.keyUp('up')
            time.sleep(0.4)
            count = count + 1
            print(count, 'up')
            if count == 10:
                print('PHASE 3 DONE AT 10')

        time.sleep(3)
        print("Calling shiny determined...")
        shinyDetermined()

bigLoop()