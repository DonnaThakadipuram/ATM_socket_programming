#name: donna thakadipuram
#date: 11/21/2023

import socket

global balance
balance = 100

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12234
server_socket.bind(('127.0.0.1', port))

server_socket.listen(1)
print("Server is listening")
c, addr = server_socket.accept()

while True:

    req = c.recv(1024).decode()
    print(req)

    #if the request has the word deposit in it, then the server will deposit the amount
    if("deposit" in req):
        req = req.split()
        balance += int(req[1])
        c.send("\nDeposit successful".encode())
        pass

    #if the request has the word withdraw in it, then the server will withdraw the amount
    elif("withdraw" in req):
        req = req.split()
        if(int(req[1]) > balance):
            c.send("\nWithdraw unsuccessful".encode())
            pass
        else:
            balance -= int(req[1])
            c.send("\nWithdraw successful".encode())
            pass
        pass

    #if the request has the word balance in it, then the server will send the balance to the client
    elif("balance" in req):
        c.send(str(balance).encode())
        pass

    #if the request has the word exit in it, then the server will close the connection
    elif("exit" in req):
        #close the connection to the client, but keep the server running for other clients
        c.close()
        server_socket.listen(1)
        print("Server is listening")
        c, addr = server_socket.accept()
        pass

