import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def backgroundCheck():
    for i in range(260,330):
        for j in range(150,200):
                if data[i, j] > 170:
                    return True
                elif data[i, j] < 100:
                    return False
                    
def isCollide(data):
    check = backgroundCheck()
    if check == True:
        for i in range(320,390):
            for j in range(390,465):
                if data[i, j] < 100:
                    hit("up")
                    return
    elif check == False:
        for i in range(320,390):
            for j in range(390,465):
                if data[i, j] > 100:
                    hit("up")
                    return
    return

if __name__ == "__main__":
    time.sleep(2)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
            
        # for i in range(340,390):
        #     for j in range(380,465):
        #         data[i, j] = 0
                
        # image.show()
        # break