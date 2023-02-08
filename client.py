from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM

#Criação de um socket genérico
myClientSocket = socket(AF_INET, SOCK_STREAM)
myClientSocket.connect(('127.0.0.1', 9091))

while True:
    msg = input ("envie uma mensagem: ")
    myClientSocket.send(msg.encode())
    data = myClientSocket.recv(2048)
    reply = data.decode()
    print(f'A resposta da solicitação foi {reply}')
