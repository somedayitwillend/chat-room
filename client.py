import socket
import threading

username = input("Choose a username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55695))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "Input USERNAME":
                client.send(username.encode('ascii'))
            else:
                print(message)
        except:
            print("Something went wrong!")
            client.close()
            break

def write():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode('ascii'))

receiveThread = threading.Thread(target=receive)
receiveThread.start()

writeThread = threading.Thread(target=write)
writeThread.start()
