import pyautogui

with open('veremos.txt', 'r') as ver:
    for line in ver:
        pyautogui.typewrite(line)
        pyautogui.press("tab")
        if line == "Opción 1":
            pyautogui.press("space")
        else:
            pyautogui.press("enter")
