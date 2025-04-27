# client/client_timeout_test.py

import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 60001)

try:
    client_socket.connect(server_address)
    print("Connected to server. Not sending any data...")

    # Just sleep and stay connected without sending
    time.sleep(60)  # Stay connected for 60 seconds (enough time to test server timeout)

finally:
    client_socket.close()
    print("Connection closed by client.")