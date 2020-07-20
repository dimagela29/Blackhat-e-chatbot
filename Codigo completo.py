def sum(number_one, number_two):
    number_one_int = convert_integer(number_one)
    number+two_int = convert_integer(number_two)
result = number_one_int + number_two_int
return result

def convert_integer(number_string):
    converted_integer = int(number_string)
    return converted_integer

asnwer = sum ('1', '2')
return converted_integer

#criando cliente tcp

import socket
target_host = "www.devtrybe.com"
target_port = 80

#criando um objeto socket

client = socket.socket(socket.AF_INET, soket.SOCK_STREAM)

#FAZ O CLIENTE SE CONECTAR
client.connect((target_host,target_port))

#envia alguns dados
client.send("GET /HTTP/1.1\r\nHost:devtrybe.com\r\n\r\n")

#recebe alguns dados 
response = client.recv(4096)
print('response')

#criando cliente udp
import socket
target_host = "127.0.0.1"
target_port = 80

#criando um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#ENVIA ALGUNS DADOS 
client.sendto("AAABBBCCC", (target_host, target_port))

#recebe alguns dados 
data, addr = client.recvfrom(4096)

print ('data')

#Criando servidor tcp
import socket 
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)

print("[*] listening on %s:%d")% (bind_ip,bind_port)

#esa é a thread para tratamento dos clientes
def handle_client(cliente_socket):
    #exibe o que o cliente enviar
    request = client.socket.recv(1024)
    print ("[*] received: %s")% request
    
    #envia um pacote de volta
    client_socket.send("ACK!")
client_socket.close()

while true:
    client,addr = server.accept()
    print(" [*] Accepted connection from: %s:%d" % (addr[0],addr[1])
#coloca nossa threadde cliente em ação para tratar os dados de entrada
client_handler = threading.thread(target=handle _client, args =(client,)
client_handler. start()
#substituindo netcat
import sys 
import socket
importgetpot
import trhreading
import subprocess

#define algumas variaveis globais 
listen = false
command = false
upload = false
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print("BHP Net Tool")
    print
    print("Usage: bhpmet.py -t target_host -p port")
    print("-l --listen      -listeb=n on[host]:[port] for incoming connections")
    print("-e --execute  =file_to_run - execute the given file upon receiving connection")
    print("-c -- command    - initialize a command shell")
    print("-u --upload=destination - upon receiving  conncetion upload a file and write to [detination]")
    print
    print
    print('Examples")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -c")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c\\target.exe")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/password\"")
    print("echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135")
    sys.exit(0)
    
    def main():
        global listen
        global port
        global execute
        global command
        global upload_destination
        global target
if not len(sys,argv[1:]):
    usage()
    
#lê as opções da linha de comando 
    try: 
        opts, args - getopt.getopt(sys.argv[1:], "hle:t:p:cu:" ["help", "listen", "execute", "target", "port", "command", "upload"]) except getopt.GetoptError as err:
            print("str(err))
            usage()
for o,a in opts:
    if o in ("-h", "--help"):
        usage()
    elif o in ("-l", "--listen"):
        listen = True
    elif o in ("-e", "--execute"):
        execute = a
    elif o in ("-c", "--command shell"):
        command = True 
    elif o in ("-u", "--upload"):
        upload_destination = a
    elif o in ("-t", "--target"):
        target = a 
    elif o in ("-p", "--port"):
        port = int(a)
    else:
        assert False, "Unhandle Option"
#iremos ouvir ou simplesmente enviar dados de stdin?
        if not listen and len(target)and port > 0:
            #le o buffer da linha de comando 
            #isso causara um bloqueio, portanto envie um CTRL-D se não estiver enviando dados de entrada para stdin
            buffer = sys.stdin.read()
            
            #iremos ouvir a porta e potencialmente, faremos upload de dados, executaremos comandos e deixaremos um shell de acordo com as opções de linha de comando anteriores
            if listen: 
                server_loop()
main()

    