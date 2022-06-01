# RSA Algorithm

# Message Receiver

from RSA_Decrypter import *
import os
from socket import *


s = socket()
# host = gethostname()
host = ""#"127.0.0.1"
port = 13000 #ports after 6000 are free

s.bind((host,port))
s.listen(10)


file = open('keys.json','rb')
print("Waiting for message")

while True:
    c, addr = s.accept()
    # print("Client connected",addr)
    #print ("Got Connection from" ,addr)
    l = c.recv(1024)
    while (l):
        file.write(l)
        l = c.recv(1024)
    file.close()
    # content=c.recv(1024).decode()
        
    print("Decrypting")
    RSA_decrypt("keys.json")
    # if data == "exit":
    #     break

s.close()
os.exit(0)
################################## ROUGH ##################################  


# UDPSock = socket(AF_INET, SOCK_DGRAM)
# UDPSock.bind(addr)

# f = open('keys.json','rb')

# print("Waiting to receive messages...")

# while True:
#     (c, addr) = UDPSock.accept()#recvfrom(buf)
#     # print("Received message: " + data.decode())
#     l = c.recv(1024)
#     while (l):
#         f.write(l)
#         l = c.recv(1024)
#     f.close()

#     print("Decrypting")
#     RSA_Decrypter()

#     if data == "exit":
#         break

# UDPSock.close()
# os._exit(0)




# s = socket()
# #host = gethostname()
# host=""
# port=13000 #ports after 6000 are free

# s.bind((host,port))
# s.listen(10)

# file = open('keys.json','wb')

# # # f = open('keys.json','wb')
# # # print("Waiting to receive messages...")

# while True:
#     c, addr = s.accept()
#     print("Client connected",addr)
#     #print ("Got Connection from" ,addr)
#     l = c.recv(1024)
#     while (l):
#         file.write(l)
#         l = c.recv(1024)
        
# #     with open('keys_server.json', 'w+') as fp :
# #         json.dumps(file, fp)


#     # f.close()
    
#     print("Decrypting")
#     RSA_decrypt("keys.json")

#     # if data == "exit":
#     #     break

# s.close()
# os.exit(0)