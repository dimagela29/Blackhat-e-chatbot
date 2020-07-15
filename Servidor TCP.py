import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(bind_ip,bind_port)

server.listen(5)

print "[*] Listening on %s%d" % (bind_ip,bind_port)

#esta щ nossa thread para tratamento de clientes

def handle_client(cliente_socket):
    
print "[*] Receveid: %s" % request

# envia um pacote de volta 
client_socket.send("ACK!")

cliente_socket.close()

while True:
    client,addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1]
# coloca nossa thread  de cliente em чуo para tratar dados de entrada 

client_handler = threading.Thread(target=handle_client,args=(client))
client_handler.start()
