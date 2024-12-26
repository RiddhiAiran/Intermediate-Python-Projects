import time
import os

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def typing(message, delay=0.05):
    """Print a message with a typing effect."""
    for letter in message:
        print(letter, end='', flush=True)
        time.sleep(delay)

def hold_screen(message="Press Enter to continue..."):
    """Hold the screen until the user presses Enter."""
    input(message)

def get_input(prompt, is_float=False, is_int=False):
    """Get user input with typing effect, either integer or float."""
    typing(prompt)
    user_input = input()
    if is_float:
        return float(user_input)
    elif is_int:
        return int(user_input)
    else:
        return user_input