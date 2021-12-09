import os
import pyautogui
import time

os.startfile(r'C:\Example_File.txt')
time.sleep(3)
pyautogui.write('Hello There', interval = 0.1)
pyautogui.press('enter')
pyautogui.write('What is the Weather?', interval = 0.1)
pyautogui.hotkey('alt', 'f4')
pyautogui.press('enter')