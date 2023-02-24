import webbrowser
import pyautogui as pt
import time
number=input("enter your nnumber ")
text= input("enter your text")
num="+91"+ number
webbrowser.open(f"https://wa.me/{number}?")
i=1
while i!=0:
    time.sleep(6)
    pt.typewrite(text)
    pt.press("enter")
    i-=0
