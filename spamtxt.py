import time
import pyautogui

message = "your text"
n = 10
time.sleep(3)

for i in range(n):
    pyautogui.typewrite(message + '\n')
