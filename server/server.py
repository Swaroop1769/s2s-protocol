# server/server.py

import socket
import threading
import time

class S2SServer:
    def __init__(self, host='localhost', port=60001, timeout=30):
        self.host = host
        self.port = port
        self.timeout = timeout

    def handle_client(self, connection, client_address):
        print(f"Connection from {client_address}")
        buffer = ""
        last_data_time = time.time()

        connection.settimeout(1.0)  # Check every second for timeout

        while True:
            try:
                data = connection.recv(1024)
                if data:
                    last_data_time = time.time()
                    buffer += data.decode()

                    if "SOF" in buffer and "EOF" in buffer:
                        start = buffer.index("SOF") + len("SOF\n")
                        end = buffer.index("\nEOF")
                        actual_message = buffer[start:end]
                        print("Complete message received:", actual_message)
                        buffer = ""

                else:
                    break

            except socket.timeout:
                if time.time() - last_data_time > self.timeout:
                    print(f"Connection with {client_address} timed out after {self.timeout} seconds.")
                    break

        connection.close()

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Server is listening on {self.host}:{self.port}...")

        while True:
            connection, client_address = server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(connection, client_address))
            client_thread.start()


if __name__ == "__main__":
    server = S2SServer()
    server.start()