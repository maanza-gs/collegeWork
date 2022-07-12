from socket import *
import subprocess

#Connect to the server
serverLocalIp = subprocess.run(['ipconfig', 'getifaddr', 'en0'], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip()
print(serverLocalIp)
serverPort=14000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverLocalIp,serverPort))

#Initializations
message = None
received_message = None

def waitUntilServerReadsTheMessage():
    received_message = clientSocket.recv(1024)
    if received_message.decode() == str(700):
        return


while True:
    received_message=clientSocket.recv(1024)
    clientSocket.send(str(700).encode())
    received_message_decoded = received_message.decode()
    if received_message_decoded == 'Menu:\n1. Register\n2. Login\n3. Exit':
        # printFancy(received_message_decoded,0.02)
        print(received_message_decoded)
        message = input('Selection: ')
        clientSocket.send(message.lower().encode())
        if message == '3':
            break
    elif received_message_decoded == 'Register!' or received_message_decoded == 'Login!':
        message = input('Username: ')
        clientSocket.send(message.encode())
        waitUntilServerReadsTheMessage()
        message = input('Password: ')
        clientSocket.send(message.encode())
    elif received_message_decoded == 'Exit!':
        break
    elif received_message_decoded == 'mag':
        message = input('Make A Guess: ')
        clientSocket.send(message.lower().encode())
    elif received_message_decoded == 'dywpa':
        message = input('Do you want to play again?(y/n): ')
        while message.lower() != 'y' and message.lower() != 'n':
            print('Undefined response. Only (y/n) allowed.')
            message = input(received_message_decoded)
        clientSocket.send(message.lower().encode())
        if message.lower() == 'n':
            break
    else:
        print(received_message_decoded)


clientSocket.close()