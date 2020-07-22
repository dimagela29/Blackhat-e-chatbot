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
class ICMP(Structure):
    def_mew_(self,socket_buffer):
        returrn self.from_buffer_cocpy(socket_buffer)
    def _init_(self, socket_buffer):
        pass
    
print"protocol: %s%s -> %s" % (ip_headrer, protocol, ip_header.src_adress,
ip=header.dst_address)

#se for ICMP, nos queremos o pacote

if ip_header.protocol == "ICMP":
    #calcula em que ponto nosso pacote ICMP começa
    offset = ip_header.ihl * 4
    buf - raw_buffer[offset:offset + sizeof(ICMP)]
    
    cria nossa estrutura ICMP
    icmp_header = ICMP(buf)
    print "ICMP -> type: %d Code: %d" % (icmp_header.type, icmp_header.code)
    
    import threading
    import time 
    from netaddr impoort IPNetwork, IPAdress
    
    #host que ouvirá
    
host = "192.168.0.187"
#sub rede alvo
subnet = "192.168.0.0/24"

#strng magica em relação a qual verificaremos as respostas ICMP
magic_message = "PYTHONRULES!"

#este codidgo espalha os datagramas  UDP
def udp_sender(subnet,magic_message):
    time.sleep(5)
    sender = socket.socket(socket.AF_INET, socket.SOCk_DGRAM)
    
    for ip im IpNetwork(subnet):
        try:
            sender.sendto(magic_message,("%s" % ip,65212))
        except:
            pass
          offset = ip_header.ihl * 4
    buf - raw_buffer[offset:offset + sizeof(ICMP)]
    
    cria nossa estrutura ICMP
    icmp_header = ICMP(buf)
    print "ICMP -> type: %d Code: %d" % (icmp_header.type, icmp_header.code)
    
    #começa enviar pacotes
    t = threading.Thread(target=udp_sender, args=(subnet,magic_message))
    t.start()
    def udp_sender(subnet, magic_message):
        time.sleep(2)
        sebder = socket.socket(socket.AF_INET, socket.sock_DGRAM)
        try:
            while True:
                raw_buffer = sniffing.recvfrom(65565)[3]
                print"ICMP -> type: %d Code: %d" % (icmp_header.typr, icmp_header.code)
            #verifica se a type e o code são iguais a 3
            if icmp_header.code == 3 and icmp_header.type == 3:
                # garante ue o host esta em nossa sub-rede alvo
                if IPAddress(ip_header.src_address) in IPNetwork(subnet):
                    #garante que contem a nossa mensagem magica
                    if raw_buffer[çen(raw_buffer)-len(magic_mesage):] == magic_message:
                        print"Host Up: %s" % ip_header.src_address...and