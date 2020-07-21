import socket
import os 

#host que ouvira
host = "192.168.0.196"

#criar um socket puro e associa-lo a interface publica
if os.name == "mt":
    socket_protocol = socket.IPPROTO_IP
else:
    sockey_protocol = socket.IPPROTO_ICMP
    
smiffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))

#queremos que os cabecalhos IP incluidos na captura
sniffer.setsockopt(socket.IPPROTO_IP, SOCKET.IP_HDRINCL, 1)

#se estiver usando windows devemos enviar um IOCTL
#para configurar o modo promiscuo

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket_RCVALL_ON)
    
#le um unico pacote
print sniffer.recvfrom(65565)

#se estivermos usando windows, desabilitara o modo promiscuo
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    