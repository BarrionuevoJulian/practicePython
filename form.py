import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLSdr-Rzkk9Vu-KR6hRyZ1fbk7Qq06aS6Y_EcCXUDBQgZaFOfvg/viewform')

sleep(2)

with open('tan.txt','r') as file:
    for line in file:
        pyautogui.typewrite(line)
        if file.read == "Opcion 1":
            pyautogui.press("space")
            pyautogui.press("enter")
            sleep(4)
        else:
            pyautogui.press("enter")
        pyautogui.press("tab")