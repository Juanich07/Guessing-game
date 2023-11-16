import socket
import random

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.33.183'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(conn.recv(1024).decode())
        attempts += 1

        if guess == secret_number:
            message = f"Congratulations! You guessed the number {secret_number} in {attempts} attempts."
            conn.send(message.encode())
            break
        elif guess < secret_number:
            conn.send(b"Too low. Try again.")
        else:
            conn.send(b"Too high. Try again.")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()