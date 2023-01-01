import keyboard

# Basic functionality for copy hotkey
keyboard.add_hotkey("Alt+C", lambda: print("Alt+C pressed"))
keyboard.wait()