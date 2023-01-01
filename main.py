import keyboard

def main():
    """Entry point upon hotkey press"""
    print("Hotkey pressed")


# Basic functionality for copy hotkey
keyboard.add_hotkey("Alt+C", main)
keyboard.wait()