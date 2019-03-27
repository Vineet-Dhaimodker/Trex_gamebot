from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (480, 505)
    dinosaur = (188, 531)
    # x = 320 (cordinate to check for tree)
    # y = 415 (cordinate of half tree

def restartGame():
    pyautogui.click(Cordinates.replayBtn)
    pyautogui.keyDown('down')

def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print('Jump')
    time.sleep(0.12)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():
    box = (Cordinates.dinosaur[0]+ 40, Cordinates.dinosaur[1], Cordinates.dinosaur[0] + 175 , Cordinates.dinosaur[1]+10)
    image = ImageGrab.grab(box) 
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return(a.sum())


def main():
    restartGame()
    while True:
        if(imageGrab() !=3537):
            pressSpace()   
            time.sleep(0.12) 
              
main()