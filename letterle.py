import random
import time

def generate_mystery_letter():
    return random.choice("abcdefghijklmnopqrstuvwxyz")

def play_letterle():
    mystery_letter = generate_mystery_letter()
    attempts = 0
    guessed_letters = ""
    print("Welcome to Letterle! If you'd like to recieve your keyboard back to normal, solve this game.")
    while True:
        guess = input("Enter a lowercase letter: ")
        guess.lower()
        attempts += 1
        if len(guess) > 1:
            print("Hey dumbass, guess one letter at a time.")
            time.sleep(0.5*attempts)
        
        if guess == mystery_letter:
            print(f"Congratulations, you guessed the mystery letter '{mystery_letter}' in {attempts} attempts!")
            break
        if guess != mystery_letter and len(guess) == 1:
            guessed_letters += guess
            print(f"Sorry, '{guess}' is not the mystery letter. Here are the guessed letters so far: {guessed_letters}")
            time.sleep(0.5*attempts)


play_letterle()

#testing name and push updates: