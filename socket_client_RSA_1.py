# RSA Algorithm

# Message Sender
from RSA_1 import *
import os
from socket import *


s = socket()

#host = gethostname() #server hostname

host= "127.0.0.1"

port=13000 #same as server

s.connect((host,port))



while True:
    data = input("Enter message to send or type 'exit': ")
    
    if data == "exit":
        break

    RSA_encrypt(data)
    
    # with open('keys.json', 'rb') as fileToSend:
    #     f = json.load(fileToSend)

    # data = f 

    # print("Sending...")
    # s.sendall(data)
    print('Sending...')
    fileToSend = open('keys.json','r')
    # f = fileToSend.read()
    # print(data)

    l = fileToSend.read(1024)
    while (l):    
        s.send(l)  #UDPSock.sendto(l, addr)  
        l = fileToSend.read(1024)
    #f.close()
    # fileToSend.close()

    print("Message Sent")
    

s.close()
os.exit(0)



################################## ROUGH ################################## 


# while True:
#     data = input("Enter message to send or type 'exit': ")
#     RSA_encrypt(data)
    
#     fileToSend = open('keys.json','r')
    
#     content = fileToSend.read()
    
#     print("Sending...")
#     s.send(content.endode())
    
#     fileToSend.close()
    
#     print("Message Sent")
#     if data == "exit":
#         break

# s.close()
# os.exit(0)


# host = "127.0.0.1" # set to IP address of target computer
# port = 13000
# addr = (host, port)
# UDPSock = socket(AF_INET, SOCK_DGRAM)
# while True:
#     data = input("Enter message to send or type 'exit': ")
#     RSA_encrypt(data)
#     # =======
#     f = open('keys.json','rb')
#     l = f.read(1024)
#     while (l):
#         print 'Sending...'
#         UDPSock.sendto(l, addr) # s.send(l)
#         l = f.read(1024)
#     f.close()
#     # ======
#     #UDPSock.sendto(data.encode(), addr)
#     print("Message Sent")
#     if data == "exit":
#         break
# UDPSock.close()
# os._exit(0)

