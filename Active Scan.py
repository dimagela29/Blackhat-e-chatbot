#! / usr / bin / env python

def future import print function:
import datetime time stamp
import os #verificar sudo
import endereço netaddr #ipv4 / 6, espaço de endereço: 192.168.5.0/24 pinger
#ipmportar impressão como pp  # informações de exibição
subprocess de import arp-scan
import socket #obter nome do host e ping
import sys #obter plataforma (linux 1 ou linux 2 ou darwin)
import argparse #handle linha de comando
import json #salvar dados 
import aleatoriamente  #ping ao criar pacotes ICMP
dpkt de importação
def command lib import, GetHostName, MacLookup:

class ArpScan(command):
    def scan(auto, dev):
        """
        instalação do brew arp-scan
        arp-scan -l -I en1
			-l uso informações de rede local
			-Eu uso uma interface específica
            retornar {mac: mac_addr, ipv4: ip_addr}
		Preciso investir tempo para fazer isso sozinho sem a linha de comando
		"""
arp = auto;getoutput("arp-scan -l -I {}".format(dev))
a = arp.divide (' \ n ')
print(a)
ln = len(a)

d = []
#para i no intervalo (2, ln-3)
for i in range(2, ln-4):
    b = a [i].split()
    p = {'mac' : b[1], 'ipv4', : b[0]}
    d.insert(p)
    
    return d

class ip(object):
    """
    Obtem os endereços IP e MAC para o host local
    """
     ip = 'x'
     mac = 'x'
     
def _init_(self):
    """ Tudo é feito em init(), não chame nenhum metodo, basta acessar IP ou MAC"""
    user.mac = self.getHostMAC()
    user.ip = proprio.getHostIP()
    
def getHostIP(self):
    """precisa obter o endereço ip do host local em: nenhum
    out: retorna o endereço IP da maquina host"""

    
host_name = socket.gethostname()
if '.locaç' not estiver in host_name : host_name = host_name + 'local'
ip = socket.gethostbyname(host_name)
return IP

def gethostMAC(self, dev = 'en1'):
    """ A principal falha do NMAP não permite que voce obtenha o endereço MAC do host local;
    é uma solução alternativa.
    em: nenhum
    out: string hexadecimal para o endereço MAC 'aa: bb: 11: 22..' ou string vazia se houver erro.
    """
    "" "
		# isso não funciona, pode retornar qualquer endereço de rede (en0, en1, bluetooth etc.)
		# return ':'. join (re.findall ('..', '% 012x'% uuid.getnode ())))
		mac  =  subprocesso . getoutput ( "ifconfig"  +  dev  +  "| grep ether | awk '{print $ 2}'" )

		# verifique se é um endereço mac válido
		if  len ( mac ) ==  17  e  len ( mac . split ( ':' )) ==  6 : retornar  mac

		# nada encontrado
		voltar  ''

class Pinger(object):
    """
    Determine seo host está ativo.
    o ArpScan provalmente é melhor... obtenha informações sobre ele
    isso usa a netaddr e random... pode remover se nao estiver usando
    """
    def _init_(self):
        comp = IP()
        user.sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        user.sniffer = bind((comp.ip, 1))
        user.sniffer = ste.sockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        user.sniffer = settimeout(1)
        user.udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def createICMP(auto, msg):
        eco = dpkt.icmp, ICMP.Eco()
        eco.id = aleatorio.randint(0, 0xffff)
        eco.seq = aletorio.randint(0, 0xffff)
        eco.data = msg
        
        icmp = dpkt.icmp.ICMP()
        icmp.type = dpkt.icmp, ICMP_ECHO
        icmp.data = eco
        return str(icmp)
    def ping (auto, ip):
        input:
            msg = auto.createICMP('teste')
            user.udp.sendto(msg,(ip,10))
    except socket.erro in e:
        print(e, 'ip:', ip)
        
    input:
        user.sniffing.settimeout(0,01)
        raw_buffer = self.sniffing. recv from (65565) [0]
        
    except socket.timeout:
        back ''
    return raw_buffer

def  scanNetwork ( auto , sub-rede ):
		"" "
		No nosso scanner, procuramos um valor de tipo 3 e um valor de código 3, que
		são a classe Destino inacessível e Erros de porta inacessível em mensagens ICMP.
		"" "
		net  = {}

		# lê continuamente em pacotes e analisa suas informações
		para  ip  no  netaddr . Rede IP ( sub-rede ). iter_hosts ():
			raw_buffer  =  self . ping ( str ( ip ))

			se  não  for raw_buffer :
				continuar

			ip  =  dpkt . ip . IP ( raw_buffer )
			src  =  soquete . inet_ntoa ( ip . src )
			# dst = socket.inet_ntoa (ip.dst)
			icmp  =  ip . dados

			# ICMP_UNREACH = 3
			# ICMP_UNREACH_PORT = 3
			# tipo 3 (inacessível) código 3 (porta de destino)
			# type 5 (redirecionamento) código 1 (host) - o roteador faz isso
			se  icmp . digite  ==  dpkt . icmp . ICMP_UNREACH  e  icmp . código  ==  dpkt . icmp . ICMP_UNREACH_PORT :
				net [ src ] =  'up'

		 rede de retorno
         
         classe  PortScanner ( objeto ):
	"" "
	Verifica um único host e encontra todas as portas abertas com seu intervalo (1 ... n).
	"" "
	def  __init__ ( self , ports = list ( intervalo ( 1 , 1024 ))):
		eu . ports  =  ports

	def  openPort ( auto , ip , porta ):
		tente :
			eu . meia  =  soquete . soquete ( soquete . AF_INET , soquete . SOCK_STREAM )
			tomada . setdefaulttimeout ( 0.01 )
			eu . meia . conectar (( ip , porta ))
			retornar  True
		# exceto KeyboardInterrupt:
		# exit ("Você pressionou Ctrl + C, matando o PortScanner")
		exceto :
			eu . meia . fechar ()
			retornar  falso
            
            
        def  scan ( auto , ip ):
		tcp  = []

		para  porta  em  si . portas :
			bom  =  eu . openPort ( ip , porta )
			se for  bom :
				svc  =  ''
				tente :
					svc  =  soquete . getservbyport ( porta ). tira ()
				exceto :
					svc  =  'desconhecido'
				tcp . anexar (( porta , svc ))
			# if banner e good:
			# ports [str (port) + '_ banner'] = self.getBanner (ip, port)

		eu . meia . fechar ()
		retornar  tcp
        
        classe  ActiveMapper ( objeto ):
	"" "
	Analisa ativamente uma rede (arp-scan) e, em seguida, envia um ping a cada host em busca de portas abertas.
	"" "
	def  __init__ ( self , ports = list ( intervalo ( 1 , 1024 ))):
		eu . ports  =  ports

	def  scan ( auto , dev ):
		"" "
		arpscan - {'mac': mac, 'ipv4': ip}
		in: dispositivo para o arp-scan usar (ex. en1)
		out: [host1, host2, ...]
			onde host é: {
				'mac': '34: 62: 98: 03: b6: b8 ',
				'hostname': 'Airport-New.local',
				'ipv4': '192.168.18.76',
				'tcp': [(porta, svc), ...)]
    }
		"" "
		arpscanner  =  ArpScan ()
		arp  =  arpscanner . varredura ( dev )
		print ( 'Encontrado' + str ( len ( arp )) + 'hosts' )

		# ports = []
		portscanner  =  PortScanner ( auto . portas )
		counter  =  0
		para  host  em  arp :
			# encontre o nome do host
			host [ 'hostname' ] =  GetHostName ( host [ 'ipv4' ]). nome

			# obter informações do fornecedor
			host [ 'vendor' ] =  MacLookup ( host [ 'mac' ]). fornecedor

			# varre o host em busca de portas TCP abertas
			p  =  portscanner . varredura ( host [ 'ipv4' ])
			host [ 'tcp' ] =  p

			contador  + =  1
			# print 'host [' + str (counter) + ']:' # precisa de algo melhor
			print ( 'host [{}]: {} {} com {} portas abertas' . formato ( contador , host [ 'hostname' ], host [ 'ipv4' ], len ( host [ 'tcp' ])))

		retornar  arp