# client/client.py

import socket
import time

class S2SClient:
    def __init__(self, host='localhost', port=60001, max_retries=3, retry_delay=2):
        self.host = host
        self.port = port
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def send_message(self, message):
        retries = 0

        while retries < self.max_retries:
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((self.host, self.port))

                try:
                    full_message = f"SOF\n{message}\nEOF"
                    client_socket.sendall(full_message.encode())
                    print("Message sent successfully!")
                finally:
                    client_socket.close()
                break

            except (ConnectionRefusedError, socket.error):
                print(f"Connection failed (attempt {retries + 1}/{self.max_retries}). Retrying in {self.retry_delay} seconds...")
                retries += 1
                time.sleep(self.retry_delay)

        if retries == self.max_retries:
            print("Failed to connect to the server after multiple attempts. Exiting.")

if __name__ == "__main__":
    client = S2SClient()
    client.send_message("Hello World")