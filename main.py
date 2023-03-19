import keyboard
import random

def shuffle_alphabet():
    print("Shuffling alphabet keys...")
    keys = keyboard.alphabet_keys
    mapping = {}
    for key in keys:
        mapping[key] = random.choice(keys)
    for key in keys:
        keyboard.press(key)
        keyboard.press(mapping[key])
        keyboard.release(mapping[key])
        keyboard.release(key)
    print("Alphabet keys shuffled!")

