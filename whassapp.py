import pyautogui
import webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=+5491127319771')

sleep(8)

with open('tan.txt', 'r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")