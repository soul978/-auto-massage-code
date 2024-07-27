import pyautogui
import time
time.sleep(2)
count = 0
while count <=1:
    pyautogui.typewrite(str(count)+" . hello ")
    pyautogui.press("enter")
    count = count+1;
