import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLSdr-Rzkk9Vu-KR6hRyZ1fbk7Qq06aS6Y_EcCXUDBQgZaFOfvg/viewform')

sleep(2)

with open('song.txt', 'r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("tab")
        if line == "Opción 1":
            pyautogui.press("space")
     	else:
            pyautogui.press("space")