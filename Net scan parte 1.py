#! / usr / bin / env python

de_future_import print function
#ipmport datetime #time stamp

import pcapy #mapeamento passivo
import os #check sudo
import pacotes de analise dpkt
import binascii #get mac addr on messages ARP# 
#import netaddr #endereços ipv4 / 6, espaço de endereço: 192.168.5.0/24
import impressão como pp # informações de exibição
#comandos de importação #arp-scan
#solicitações de importação #mac api
soquete de importação #pedido
import sys #obter plataforma (linux ou linux2)
#subprocesso de importação #use commandline
#importrandom #pinger o usa ao criar pacotes ICMP
#da lib import WhoIs
#do wol de importação acordado #wake on lan

"""
sudo tcpdump -s 0 -i en1 -w test.pcap
-s 0 definirá o byte de captura para seu máximo ou seja 65535 e não truncará
-i en1 capturará a interface Ethernet
-w test.cap criará esse arquivo pcap

tcpdump -qns 0 -X -r osx.pcap

$sudo tcpdump -w osx.pcap
tcpdump: tipo de link de dados PKTAP
tcpdump: escutando no pktap, PKTAP do tipo link (Tapet Tap), tamanho da captura 65535 bytes
^ Pacotes C4414 capturados 
4416 pacotes recebidos pelo filtro
0 pacotes descartados pelo kernel"""


"""



#######################
# class DNS (objeto):
# def __init (self, udp) __:
# dns = dpkt.dns.DNS (udp.data)
# para rr em dns.an:
# h = self.getRecord (rr)
# print h
"""
classe ARP(objeto):
    def _init_(self, arp):
        user.msg = {}
        se arp.op == dpkt.arp. ARP_OP_REPLY:
            user.msg: {
                    'type': 'arp', 
                    'mac': self.add_colons_to_mac(bininas.heslify(arp, sha))
                    'ipv4': soquete.inet_ntoa(arp.spa)
                    }
            return
        def get(próprio):
            return user.msg
        
        def add_colons_to_mac(self, mac_addr):
            """
            Está função aceita uma sequencia de 12 digitos hexadecimais e a converte em dois pontos
            sequencia separada
            """
            
            s = lista()
            for i in range(12 / 2): #mac_addr deve ser sempre 12 caracteres, trabalhamos em um grupo de 2 digitos
                s.acrescentar(mac_addr [i * 2 : I * 2 + 2])]
    r = ":" . junção(s)
    return r

class mDNS(objeto):
    def _init_(self, udp):
        user.msg = {}
        tente: 
            mdns = dpkt.DNS.DNS(dadosdup.)
        except dpkt.error:
            #print "mDNS dpkt.Error'
            return
        except(IndexError, TypeError):
            #dpkt não deve fazer isso, mas em alguns casos
            #print "mDNS outro erro"
            return
        except:
            #print "mDNS crap:", sys.exc_info()
            #print "mDNS outro erro"
            return
        except:
             #print "mDNS crap:", sys.exc_info()
             #print udp
             return
         if mdns.qr != dpkt.DNS, DNS_R: return
         if mdns.qr.opcode != dpkt.DNS, DNS_QUERY: return
         if mdns.qr.rcode != dpkt.DNS, DNS_RCODENOERR: return
         
         user.msg[type] = 'mdns'
         ans =[]
         
         para rr em mdns.um:
             h = auto.getRecord(rr)
             #verifique se está vazio
             se h:ans.insert(h)
        user.msg['rr'] = ans
        return