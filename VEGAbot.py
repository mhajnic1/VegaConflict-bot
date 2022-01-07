from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con

time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(np.random.uniform(0.1, 0.3))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
#bilo bi tesko ugasiti program s obzirom da mice mis cijelo vrijeme
while keyboard.is_pressed('q') == False:
    
    # ODABIR FLOTE ZA KORISTENJE - biramo prvo random flotu, te nakon toga glavnu tako da popup window bude aktivan uvijek
    pyautogui.keyDown('1')
    time.sleep(np.random.uniform(0.1, 0.3))
    pyautogui.keyUp('1')

   
    pyautogui.keyDown('3')
    time.sleep(np.random.uniform(0.2, 0.4))
    pyautogui.keyUp('3')

    # cekanje izmeeđu timera je da igrica teze skuzi da je ovo skripta1
    time.sleep(np.random.uniform(0.75, 1.25))

    #PROVJERA - dali je flota u bitci 
    if pyautogui.pixel(817, 1010)[0] != 232:
        
        #EVENT SPECIFIC - provjera za blitz popup    1436 Y:  188
        if pyautogui.locateOnScreen('blitz.png', grayscale = True, confidence = 0.8) != None:
            #gasi popup
            click(1436, 188)
            
        #provjera ako slucajno napadamo s krivom flotom   X: 1056 Y:  664
        if pyautogui.locateOnScreen('alert.png', grayscale = True, confidence = 0.7) != None:
            #gasi popup
            click(1056, 664)
        
        #FREE REPAIR - provjera
       # if pyautogui.locateOnScreen('repair.png', grayscale = True, confidence = 0.8) != None:
            #FREE REPAIR AVAILABLE
       #     click(978, 928)
            
        time.sleep(np.random.uniform(1, 2))

        #Klik na find fleet za napasti
        click(1627, 94)

        #random wait
        time.sleep(np.random.uniform(1, 1.5))

        #PROVJERA BOJE PIKSELA BOTUNA ZA NAPAD
        if pyautogui.pixel(817, 1010)[0] == 232:
            #BOTUN CRVEN I SPREMAN ZA NAPASTI
            click(817, 1010)
            time.sleep(np.random.uniform(13, 15))

