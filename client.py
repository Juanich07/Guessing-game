import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.33.183'
    port = 12345

    client_socket.connect((host, port))
    print("Connected to server")

    while True:
        guess = input("Guess the number (between 1 and 100): ")
        client_socket.send(guess.encode())

        response = client_socket.recv(1024).decode()
        print(response)

        if "Congratulations" in response:
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()