def getRecord(self, rr):
 		if rr . type  ==  1 : retorna { 'type' : 'a' , 'ipv4' : socket . inet_ntoa ( rr . rdata ), 'hostname' : rr . nome }
		elif  rr . type  ==  28 : retornar { 'type' : 'aaaa' , 'ipv6' : socket . inet_ntop ( socket . AF_INET6 , rr . rdata ), 'hostname' : rr . nome }
		elif  rr . type  ==  5 : retornar { 'type' : 'cname' , 'hostname' : rr . nome , 'cname' : rr . cname }
		elif  rr . type  ==  13 : retornar { 'type' : 'hostinfo' , 'hostname' : rr . nome , 'info' : rr . rdata }
		elif  rr . type  ==  33 : retornar { 'type' : 'srv' , 'hostname' : rr . srvname , 'porta' : rr . porta , 'srv' : rr . nome . split ( '.' ) [ - 3 ], 'proto' : rr . nome . divisão ( '.' ) [ - 2 ]}
		elif  rr . type  ==  12 : retornar { 'type' : 'ptr' }
		elif  rr . type  ==  16 : retornar { 'type' : 'txt' }
		elif  rr . type  ==  10 : return { 'type' : 'wtf' }
		
		def get(proprio):
		return a user.msg

class PacketDocker(obejct):
"" "
	PacketDecoder lê pacotes dpkt e produz um ditado com informações úteis na rede
	recon. Nem tudo é usado atualmente.
	eth: hw addr src, dst
	 - ipv4: endereço IP src, dst
	   - tcp: porta src, dst; sequência num;
	   - udp: porta src, dst;
		 - dns: opcode; rcode;
		   - RR:
			 -- TXT: ?
			 - a: ipv4; nome de anfitrião
			 - aaaa: ipv6; nome de anfitrião
			 - ptr:?
			 - cname:?
			 - srv: nome do host; serviço; protocolo; porta
		   - Q:
	 - ipv6: endereço IP src, dst; nxt
	   - icmpv6:
	"" "
	
	ipMap = {}
	
	def getip(self, ip, ipv6 = false)
		ifipv6:
		return.inet_ntop(socket.AF_INET6, ip)
		add:
		return.inet_ntoa (ip)
		
	decodificação def(self, eth):
	"" "
		decodificar um pacote ethernet. O dict retornado indica o tipo (arp, mdns, etc)
		que indicará como ler / usar o ditado.
		https://support.apple.com/en-us/HT202944
		em: ethernet pkt
		out: dict
		"" "
		
		if eth.input == dpkt.ethernet.ETH_TYPE_ARP:
			return ARP(data of et).get()
		
		elif eth.input == dpkt.ethernet. ETH_TYPE_IP6:
		IP = eth.data
		if ip.p == dpkt.ip IP_PROTO_UDP:
		udp = udp.data
		
		if udp.port == 5353:
		ans = mDNS(udp).get()
		 return ans
		 
		elif ip.p == dpkt.ip, IP_PROTO_TCP:
				pass
				
		elif ip.p == dpkt.ip, IP_PROTO_ICMP6:
				pass
		
		else: 
				pass
				
elif eth.input ==  dpkt.ethernet ETH_TYPE_IP:
		ip = eth.data
		
		#porta da interface roku: 1900 dst: 239.255.255.250.1900
		if ip.p == dpkt.ip IP_PROTO_UDP:
				udp = ip.dados
		
		if udp.port == 53 :
			return {}
		
		elif udp.port == 5353:
			return mDNS(UDP).get()
			
		elif auto.getip(ip.dst) == '239.255.255.250'
				return {}
				
		else:
				return {}
		
		elif ip.p == dpkt.ip IP_PROTO_TCP:

# src = self.getip (ip.src)
				# if netaddr.IPAddress (src) não está em netaddr.IPNetwork ("192.168.1.0/24"):
				# who = ''
				# if src não está em self.ipMap:
				# who = WhoIs (src) .record ['NetName']
				# self.ipMap [src] = quem
				# outro:
				# who = self.ipMap [src]
				# if who in ['GOOGLE' ',' AKAMAI ',' APPLE-WWNET ',' AMAZO-ZIAD1 ',' DROPBOX ']:
				# Retorna {}
				# outro:
				# print src, quem
				# não imprime portas padrão
				# porta 58969 - XSANS Apple, por que vejo isso?
				# 22 ssh
				# 25 smtp
				# 80 http
				Servidor de horário # 123
				# 143 imap
				# 443 https
				# 445 smb
				# 548 afp sobre tcp
				# 5009 utilitário de administração do aeroporto
				# 5222 ichat
				# 17500 dropbox
				# if not ip.data.dport in [22,25,80,123,143,443,445,548,5009,5222,17500]:
					# print 'other tcp', 'port:', ip.data.dport, 'src:', self.getip (ip.src), 'dst:', self.getip (ip.dst)
				retornar {}
				
				elif ip.p == 2:
						pass
						
				else: 
						return {}
						
class PassiveMapper (object):
	def _init_ (self):
		user.map = []
		
	process de def(self,hrd, data)
	#processa cada pacote do pcap
	eth = dpkt.ethernet. ETHERNET(data)
	a = auto.p.decoder (eth)
	if one:
				user.mapa.index(a)
	def pcap(self, frame):
	cap = pcapy.open_offline (fname)
	
	user.map = []
	user.p = packetDecoder ()
	cap.loop ( 0, auto.process)
	return a user.mapa
	
	def rr (auto, rec):
		ans = {'host do nome' : '', 'tcp', : [], 'udp' : []}
		for line in rec ['rr']:
			
			rtype = line ['tipo']
			if rtype == 'ptr':
						pass
			
			elif rtype == 'txt':
						pass
						
elif rtype == 'srv':
ans [ 'hostname' ] =  linha [ 'hostname' ]
				se  linha [ 'proto' ] ==  '_tcp' : ans [ 'tcp' ]. acrescentar ({ 'srv' : linha [ 'srv' ], 'porta' : linha [ 'porta' ]})
				 linha elif [ 'proto' ] ==  '_udp' : ans [ 'udp' ]. acrescentar ({ 'srv' : linha [ 'srv' ], 'porta' : linha [ 'porta' ]})
				mais :
					print ( 'algo aconteceu' , linha )
			# elif type == 'rr': imprime 'rr'
			 
			 elif rtype == 'aaaa':
			 ans['ipv6'] = line ['ipv6']
			 ans['hostname'] = line ['hostname']
			 
			 elif rtype = 'a':
			 ans ['ipv4'] = line ['ipv4']
			 ans['hostname'] = line['hostname']
			 
			 else: 
			 print('Algo deu errado')
			 
if not ans ['hostname'] and not ans ['tcp']
ans = {}

return ans

filtro de definição(auto, rec):
""" a saida do pcap e apenas ima lista de registros, isso condensa/combina as informações em um mapeamento de rede"""

ans = []
for line in rec:
	if 'rr' in line:
	a = auto.rr(line)
	
	if:
		a ['type'] = 'rr'
		ans.index (a)
		
	elif 'type' in line:
		rtype = linha ['tipo']
		
	if rtype == 'aaaa': ans.index(line)
	elif rtype == 'a': ans.index(line)
	eçif rtype == 'arp': ans.index(line)
	else: print ('<<<<', line, '>>>>')
add: 
	print ('*****', line, '*****')
	
return ans

def find(self, a, b):

"""encontre um registrro para o mesmo host e mescla as informçõe. se o host não puder ser encontrado, ele adciona um novo
registro para o host"""

for i in b:

if 'ipv4' in i e 'ipv4' in one:
	if user ['ipv4'] == a ['ipv4']:
	i.atualizer (a)
	return
	
elif 'ipv6' in i and 'ipv6' in one:
	if user ['ipv6] == a ['ipv6']:
	i.atualizer(a)
	return
	
elif 'hostname' in i and 'hostname' in one:
	if i ['hostname'] == a ['hostname']:
	i.atualizer(a)
	return
	
b. index(a)
return

def combine(self, map):
"""muito a fazer"""

ans = []
for host in nmap:
	user.location(host, ans)
return ans

def live (self, dev,loop = 500):
""" dispositivo aberto 
os argumentos aqui são:
dispositivo 
snaplen(numero maximo de bytes para capturar _per_packet_)
modo promiscuo(1 para true), precisa de false para OSX
tempo limite (em milisegundo)"""

#verifique os privilegios do sudo /root
if os.getuserid() != 0:
	exit (Voce precisa ser sudo/root para sair em tempo real')
	
#tempo real
cap = pcapy.open_live(dev, 2048, false, 50)
#cap setfilter('udp')

user.map = []
user.p = PacketDecoder()

#começar rastrear pacotes

while(loop):
	test:
	loop -= 1
	(cabecalho,data) = next(limit)
except KeyboardInterrupt:
print('Voce pressiona ^C, saindo do passive Mapper... Tchau')
exit()
except:
		continue
user.process(cabecalho, data)
return a user.mapa

		 	
				
		
		
	
	
	