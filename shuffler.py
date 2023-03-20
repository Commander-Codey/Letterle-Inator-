import keyboard
import time
import random

def generate_replacements():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shuffled_alphabet = random.sample(alphabet, len(alphabet))
    replacements = dict(zip(alphabet, shuffled_alphabet))
    return replacements

replacements = generate_replacements()

def on_press(event):
    if event.name.lower() in replacements:
        keyboard.press_and_release('backspace')
        time.sleep(0.001)
        keyboard.press_and_release(replacements[event.name.lower()])
        return False
    
def main():
    keyboard.on_press(on_press)
    keyboard.wait()

main()