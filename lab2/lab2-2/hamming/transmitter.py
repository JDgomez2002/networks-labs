# Universidad del Valle de Guatemala
# Redes - Laboratorio 2
# Daniel Gomez 21429

import socket
import json
from helpers.transmitter.hamming_encoder import codificateMessasge
from helpers.transmitter.hamming_calculate_integrity import calculateIntegrity
from helpers.transmitter.hamming_turbation import turbation

host = '127.0.0.1'  # The server's hostname or IP address
port = 65432        # The port used by the server

def send_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())
        response = s.recv(1024)
        print('Received from server:', response.decode())

if __name__ == "__main__":
    while True:
        print("Enter the message to send")
        message = str(input(">> "))
        # codification layer
        encoded, binaryMessage = codificateMessasge(message)

        print("------------------ Hamming algorithm ------------------")
        print("Message:", message)
        print(f"Binary message: {binaryMessage}")
        print(f"Codificated bits: {encoded}")
        print(f'length: {len(encoded)}')
        print("\n--------------------------------------------------------")

        # calculate integrity layer
        calculateIntegrity(encoded)
        # turbation layer
        encoded = turbation(encoded)
        send_message(encoded)

        print("Do you want to send another message? (y/n)")
        if input(">> ") != 'y':
            break
