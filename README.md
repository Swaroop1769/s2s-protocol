# Lightweight Server-to-Server Communication (TCP)

This project builds a simple TCP-based communication between two services (Server and Client) without using HTTP.

### Features
- Lightweight messaging using SOF/EOF markers
- Retry logic for connection failures
- Timeout handling for idle connections
- Organized code using Python classes

### How to Run

1. Start the server:
   ```bash
   cd server
   python server.py
2. Start the client:
   ```bash
   cd client
   python client.py

### Purpose

The goal of this project is to understand how microservices can communicate internally without using HTTP, and to build a lightweight TCP-based protocol for server-to-server (S2S) communication.

### Future Improvements

- Upgrade the system to use gRPC for more efficient, scalable, and structured communication.
- Define services and messages using Protocol Buffers.