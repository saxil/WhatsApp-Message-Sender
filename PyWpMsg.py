import webbrowser 
import pyautogui as pyag
Num=0
Text=0

def GetNumText():
    global Num
    global Text
    Num=int(input("Type a Number:"))
    Text= str(input("Type your Message:"))
    
def Send():
    webbrowser.open(f"https://wa.me/+91{Num}/{Text}")
    pyag.press("enter")

def Main():
    if "__name__"=="__main__":
        GetNumText()
        Num=Num
        Text=Text
        Send()
Main()

