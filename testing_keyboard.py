import keyboard
import random
import time

def main():
    # Record events until 'esc' is pressed.
    recorded = keyboard.record(until='enter')
# Then replay back at three times the speed.
    ## keyboard.play(recorded, speed_factor=3)
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+l')
    time.sleep(0.1)
    keyboard.write('youtube.com')
    time.sleep(0.1)
    keyboard.press_and_release('enter')

main()




