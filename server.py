from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from threading import Thread


#Criação de um socket genérico
myServerSocket = socket(AF_INET, SOCK_STREAM)
print("Socket criado...")
myServerSocket.bind(('127.0.0.1', 9091))
myServerSocket.listen()

def HandleRequest(mClientSock, mClientAddr):
    while True:
        data = mClientSock.recv(2048)
        req = data.decode()
        print(f'A solicitação feita pelo cliente foi {req}')
        rep = 'ok'
        mClientSock.send(rep.encode())
        print(f'Mensagem enviada...')

while True:
    clienteSock, clienteAdr = myServerSocket.accept()
    print(f'O cliente {clienteAdr} enviou uma solicitação')
    Thread(target=HandleRequest, args= (clienteSock, clienteAdr)).start()

