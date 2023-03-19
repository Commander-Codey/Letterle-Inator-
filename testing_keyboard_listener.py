from pynput import keyboard

# Define a dictionary of key mappings
key_mappings = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}

# Define a function to remap the keys
def remap_keys(key):
    try:
        # Try to remap the key using the dictionary
        return key_mappings[key.char]
    except KeyError:
        # If the key is not in the dictionary, return the original key
        return key.char

# Define a function to handle key presses
def on_press(key):
    # Get the remapped key
    remapped_key = remap_keys(key)
    
    # Type the remapped key
    keyboard.Controller().type(remapped_key)
    
    # Block the original key press from being sent to the operating system
    return False

# Start listening for key presses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
