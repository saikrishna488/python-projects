import pyautogui as gui
import time

message = input("enter message")
no = int(input("number of times"))
time.sleep(2)

for i in range(no):
    time.sleep(0.5)
    gui.typewrite(message)
    gui.press('Enter')
    