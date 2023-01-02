import keyboard
from PIL import ImageGrab, Image

def main():
    """Entry point upon hotkey press"""
    print("Hotkey pressed")

    # Get the current clipboard image
    img = ImageGrab.grabclipboard()


# Basic functionality for copy hotkey
keyboard.add_hotkey("Alt+C", main)
keyboard.wait()