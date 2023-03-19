import keyboard
import random

import keyboard
import random
import time

def shuffle_keyboard():

    keys = [key for key in keyboard.all_keys() if len(key) == 1 and key.isalpha()]

    # Shuffle the letter key positions randomly
    mapping = {}
    for key in keys:
        mapping[key] = random.choice(keys)

    # Simulate pressing and releasing each letter key in the new shuffled order
    for key in keys:
        keyboard.press(key)
        keyboard.press(mapping[key])
        keyboard.release(mapping[key])
        keyboard.release(key)

def unshuffle_keyboard():
    # Get a list of all letter keys on the keyboard
    keys = [key for key in keyboard.all_keys() if len(key) == 1 and key.isalpha()]

    # Create a mapping of the current letter key positions to the original positions
    mapping = {}
    for key in keys:
        mapping[key] = key

    # Simulate pressing and releasing each letter key in the original order
    for key in keys:
        keyboard.press(key)
        keyboard.press(mapping[key])
        keyboard.release(mapping[key])
        keyboard.release(key)

if __name__ == '__main__':
    print("Press 's' to shuffle the letter keys on the keyboard or 'u' to unshuffle them.")
    shuffle_time = 0
    while True:
        # Listen for key presses
        event = keyboard.read_event()
        if event.name == 'u':
            unshuffle_keyboard()
            break
        elif event.name == 'esc':
            break
        else:
            # if time.time() - shuffle_time < 15:
            #    continue
            shuffle_keyboard()
            # shuffle_time = time.time()

