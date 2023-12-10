#name: donna thakadipuram
#date: 11/21/2023

import socket
import sys

#setup stuff
client_socket = socket.socket()
port = 12234
client_socket.connect(('127.0.0.1', port))
print("Connection established")

while True:
    #print menu
    print("\n1. Deposit\n")
    print("2. Withdraw\n")
    print("3. Check Balance\n")
    print("4. Exit\n")

    selection = input("What would you like to do? ")

    #deposit
    if(selection == "1"):
        print("How much would you like to deposit? ")
        message = input()
        if("." in message or message == "" or message.isalpha() == True or int(message) < 0 or "-" in message):
            print("Invalid input")
            pass
        else:
            message = "deposit " + message
            client_socket.send(message.encode())
            print(client_socket.recv(1024).decode())
            pass
        pass

    #withdraw
    elif(selection == "2"):
        print("How much would you like to withdraw? ")
        message = input()
        if("." in message or message == "" or message.isalpha() == True or int(message) < 0 or "-" in message):
            print("Invalid input")
            pass
        else:
            message = "withdraw " + message
            client_socket.send(message.encode())
            print(client_socket.recv(1024).decode())
            pass
        pass

    #check balance
    elif(selection == "3"):
        client_socket.send("balance".encode())
        print("\nYour balance is: " + client_socket.recv(1024).decode())
        pass


    #exit
    elif(selection == "4"):
        client_socket.send("exit".encode())
        print("Closing connection...")
        client_socket.close()
        sys.exit()
        pass
    
    else:
        print("Invalid input")
        pass
