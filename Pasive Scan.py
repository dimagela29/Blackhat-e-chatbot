#! / usr / bin / env python

de __future__ import  print_function
# import datetime # time stamp
importar  pcapy          # mapeamento passivo
import  os             # check sudo
importar  pacotes de análise dpkt           #
import  binascii       # get MAC addr on messages ARP
# import netaddr # endereços ipv4 / 6, espaço de endereço: 192.168.5.0/24
# importar impressão como pp # informações de exibição
# comandos de importação # arp-scan
# solicitações de importação # mac api
 soquete de         importação # pedido
# import sys # obter plataforma (linux ou linux2)
# subprocesso de importação # use commandline
# import random # Pinger o usa ao criar pacotes ICMP
# da lib import WhoIs
# do wol de importação acordado # wake on lan

"""

sudo tcpdump -s 0 -i en1 -w test.pcap
-s 0 definirá o byte de captura para seu maximo ou seja 65535 e não truncará
-i en1 captura a interface ethernet
-w test.pcap criará esse arquivo pcap

sudo tcpdump -w osx.pcap
tcpdump: tipo fr link de dados PKTAP
tcpdump: escutando pktap, PKTAP do tipo link(Tapet, tap), tamanho da captura 65535 bytes
^ pacotes C4414 capturados
4416 pacotes recebidos pelo filtro
0 pacotes descartados pelo kernel

"""


#######################
# class DNS (objeto):
# def __init (self, udp) __:
# dns = dpkt.dns.DNS (udp.data)
# para rr em dns.an:
# h = self.getRecord (rr)
# print h

class ARP(obejct):
    def _init_(self, arp):
        user.msg = {}
        if arp.op == dpkt.arp. ARP_OP_REPLY:
            user.msg = {
                    'type' : 'arp',
                    'mac' : self.add_colons_to_mac(bininas.hexlify(arp.sha)),
                    'ipv4' : socket.inet_ntoa(arp.spa)
                    }
            return
   
    def get(proprio):
        return a user.msg
    
    def add_colons_to_mac(self, mac_addr):
        """ esta função aceita uma sequencia de 12 digitos hexadecimais e a converte em dois pontos"""
        
        s = lista()
        for i in range (12 / 2):
            s.sum(mac_addr[i * 2 : i * 2 + 2])
            r = ":" .junção(s)
            return R
        
class mDNS(object):
   
    def _init_(self, udp):
        user.msg = {}
        if:
            mdns = dpkt.DNS.DNS(dados udp.)
       
        except dpkt.error:
            return
        
        except(IndexError, TypeError):
            return
        
        except:
            return
        
        if mdns.qr != dpkt.DNS. DNS_R: return
        if mdns.opcode != dpkt.DNS DNS_Query: return
        if mdns.rcode != dpkt.DNS DNS_RCODE_NOERR: return
        
        user.msg ['type'] = 'mdns'
        ans = []
        
        for rr in mdns.um:
            h = auto.getrecord(rr)
            
            if h: ans.sum (h)
            
            user.msg ['rr'] = ans
            return 