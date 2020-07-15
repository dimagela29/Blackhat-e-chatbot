import socket

target_host= "127.0.0.1"
target_port

#criar um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCL_DGRAM)

#ENVIA ALGUNS DADOS 

client.sendto("AAABBBCCC" , (target_host, target_port)

#recebendo alguns dados

data, addr = cliente.recvform(4096)

print data

