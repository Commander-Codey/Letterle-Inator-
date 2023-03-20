import keyboard
import random
import time



def youtubeTest():
    recorded = keyboard.record(until='esc')
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+l')
    time.sleep(0.1)
    keyboard.write('youtube.com')
    time.sleep(0.1)
    keyboard.press_and_release('enter')


def addHotkey():
    keyboard.add_hotkey('c', lambda: keyboard.press_and_release('b', 'a'))

def main():
    #addHotkey()
    youtubeTest()

    time.sleep(20)
    keyboard.remove_all_hotkeys
main()




