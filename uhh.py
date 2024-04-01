import pyautogui
import keyboard

while True:
    if keyboard.is_pressed('b'):
        pyautogui.hotkey('f3', 'g')