import pyautogui as spam
import time
print("Shivam......")
limit = input("Enter you numbers :")
msg = input("Massage you want to send :")

i=0

time.sleep(5);

while i<int(limit):
    spam.typewrite(str(i)+" . "+msg)
    spam.press("enter")
    i=i+1;
   
