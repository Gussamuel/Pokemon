import time
import os
from pynput.keyboard import Key, Controller
import pyautogui
from PIL import ImageGrab
import imessage
import sys

sys.setrecursionlimit(10000)

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
    time.sleep(2)
    rgbShiny2 = (255, 235, 0, 255)
    rgbShiny = (255, 194, 0, 255)
    
    # Take a screenshot
    screenshot = ImageGrab.grab()
    
    # Coordinates to check
    x, y = 1524, 432  # Update these coordinates if necessary
    
    # Get the pixel value at the specified coordinates
    rgb = screenshot.load()[x, y]
    
    print(f"\nCaptured RGB value at ({x}, {y}): {rgb}")

    # After retrieving the RGB value, delete the screenshot to free memory
    del screenshot

    # Check for shiny
    if rgb == rgbShiny2:
        print(f"\n{get_var_value()} RESETS. NOT SHINY.")
    elif rgb == rgbShiny:
        print(f"\n{get_var_value()} RESETS. */*/*/* SHINY */*/*/*\n")
        shinyText(get_var_value())  # Send shiny found text
        exit()
    else:
        print(f"\n{get_var_value()} RESETS. ?????????? ERROR, SCREENSHOT TAKEN AND STORED TO DESKTOP ??????????\n")

        # Take a new screenshot for saving the error
        screenshot = ImageGrab.grab()
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        screenshot_path = os.path.join(desktop_path, "error_screenshot.png")
        screenshot.save(screenshot_path)
        print(f"SCREENSHOT SAVED TO: {screenshot_path}")

        # Explicitly delete the screenshot after saving
        del screenshot

def bigLoop():
    while True:
        count = 0
        os.system("open /Applications/Playback.app")
        print('\n********** RESET **********\n')
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

        print('\n---------- START PHASE 1 ----------\n')
        for i in range(5):
            keyboard.press('x')
            time.sleep(0.8)
            keyboard.release('x')
            time.sleep(0.8)
            count = count + 1
            print(count, 'x')
            if count == 5:
                print('\n---------- END PHASE 1 ----------\n')

        print('\n---------- START PHASE 2 ----------\n')
        for i in range(1):
            keyboard.press('z')
            time.sleep(0.8)
            keyboard.release('z')
            time.sleep(0.8)
            count = count + 1
            print(count, 'z')
            if count == 6:
                print('\n---------- END PHASE 2----------\n')

        print('\n---------- START PHASE 3 ----------\n')
        for i in range(3):
            time.sleep(0.5)
            keyboard.press('x')
            time.sleep(0.5)
            keyboard.release('x')
            time.sleep(0.5)
            count = count + 1
            print(count, 'x')
            if count == 9:
                print('\n---------- END PHASE 3 ----------\n')

        print("\n########## CALLING FUNCTION ##########")
        shinyDetermined()

# Run the main loop
bigLoop()