def getRecord(self, rr):
    """ os registros de resposta (rr) em um pacote DNS referem-se ao mesmo host
    """
    
		se  rr . type  ==  1 : retorna { 'type' : 'a' , 'ipv4' : socket . inet_ntoa ( rr . rdata ), 'hostname' : rr . nome }
		elif  rr . type  ==  28 : retornar { 'type' : 'aaaa' , 'ipv6' : socket . inet_ntop ( socket . AF_INET6 , rr . rdata ), 'hostname' : rr . nome }
		elif  rr . type  ==  5 : retornar { 'type' : 'cname' , 'hostname' : rr . nome , 'cname' : rr . cname }
		elif  rr . type  ==  13 : retornar { 'type' : 'hostinfo' , 'hostname' : rr . nome , 'info' : rr . rdata }
		elif  rr . type  ==  33 : retornar { 'type' : 'srv' , 'hostname' : rr . srvname , 'porta' : rr . porta , 'srv' : rr . nome . split ( '.' ) [ - 3 ], 'proto' : rr . nome . divisão ( '.' ) [ - 2 ]}
		elif  rr . type  ==  12 : retornar { 'type' : 'ptr' }
		elif  rr . type  ==  16 : retornar { 'type' : 'txt' }
		elif  rr . type  ==  10 : return { 'type' : 'wtf' }
def get(proprio):
    retornar a usuario.msg
    
class PacketDecoder(object):
    """
    PacketDecoder le os pacotes dpkt e produz um ditado com informações uteis na rede
    recon. Nem tudo é usado atualmente.
    eth: hw addr src, dst
    -tcp: porta src,dst; sequencia num;
    -udp: porta src, dst;
    -dns: opcode; rcode;
    -RR:
        -- TXT: ?
        a: ipv4; nome do anfitrião
        aaaa: ipv6, nome do anfitrião
        ptr:?
        cname:?
        srv: nome do host, serviço; protocolo; porta
    -Q:
ipv6: endereço IP src, dst; nxt
-icmpv6:
"""
ipMap = {}
def getip(self, ip, ipv6 = false):
    if ipv6:
        tomada de return.inet_ntop(socket.AF_INET6, ip)
    else:
        tomada de return.inet_ntoa(ip)
decodificação def(self, eth):
    """ decodificar um pacote ethernet.O dict retornado o tipo(arp, mdns, etc)
    que indicara como ler / usar o ditado.
    	https://support.apple.com/en-us/HT202944
        
        em : ethernet pkt
        out: dict
        """
if eth.digite == dpkt.ethernet.ETH_TYPE_ARP:
    "print 'ARP'"
    return ARP (data de et.).get()
elif eth.digite == dpkt.ethernet. ETH_TYPE_IP06:
    ip = eth.data
    
    #multicast é com o IPV4
    if udp.dport == 5353:
        #print udp
        ans = mDNS(udp).get()
        #print 25 * '='
        #pp.print (ans)
        #print 25 * '='
        return ans
   
    # print 'IPv6 UDP', 'porta:', udp.dport, 'src:', self.getip (ip.src, True), 'dst:', self.getip (ip.dst, True)

#tcp não é util 
    elif ip.p == dpkt.ip. IP_PROTO_TCP:
        pass
    tcp = ip.data
    #print 'IPv6 TCP', 'port:', tcp.dport, 'src:', self.getip(ip.src, true), 'dst:', self.getip(ip.dst, true)
    #msg de erro ICMP não é util para mapeamento
elif ip.p == dpkt.ip. IP_PROTO_ICMP6:
    # PRINT 'IPv6, icmp6:' ip.data.data
    pass
sum:
    pass
# print 'IPv6', ip.p, 'src:', self.getip (ip.src, True), 'dst:', self.getip (ip.dst, True)
elif eth.input == dpkt.ethernet.ETH_TYPE_IP:
    ip = eth.data
    #porta da interface Roku: 1900 dst: 239.255.255.250 1900
    if ip.p == dpkt.ip.IP_PROTO_UDP:
        udp = ip.data
    elif:
        udp.port == 53:
            return DNS (udp.data)
        return {}
    elif:
        udp.port == 5353:
            'print mDNS'
            'print udp'
             return mDNS(udp).get()
         elif.auto.getip(ip.dst) == '239.255.255.250':
             return {}
         else:
             
					# não imprime portas padrão
					# 17500 dropbox
					# se não for ip.data.dport em [17500]:
					# print 'other udp', 'port:', udp.dport, 'src:', self.getip (ip.src), 'dst:', self.getip (ip.dst), ':'
                    return {}
        elif:
            ip.p == dpkt.ip.IP_PROTO_TCP:
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
                    return {}
                elif ip.p == dpkt.ip.IP_PROTO_ICMP6:
                    # impressão '?????? outro icmp6 ',' src: ', self.getip (ip.src),' dst: ', self.getip (ip.dst)
                elif ip.p == 2:
                    pass
                # print 'IGMP', 'src:', self.getip (ip.src), 'dst:', self.getip (ip.dst)
            else:
#                print 'outro pacote IP', 'src:', self.getip (ip.src), 'dst:', self.getip (ip.dst)'
                return {}
            
                    