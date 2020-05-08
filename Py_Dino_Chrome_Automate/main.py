import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return
        
def isCollide(data):
    for i in range(260,330):
        for j in range(410,465):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    time.sleep(2)
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
            
        # for i in range(260,330):
        #     for j in range(410,465):
        #         data[i, j] = 20
                
        # image.show()
        # break