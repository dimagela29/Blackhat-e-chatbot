 #! / usr / bin / env python
# - * - codificação: utf-8 - * -

"" "Classe de Digitalização em Rede" ""

do libmap.import de process NmapProcess
do libmap analisador de importação NmapParser
immport print como pp
data e hora do import

#determina o SO
da plataforma de import do sys como_plataforma

"" "
Formato:
{'xx: xx: xx: xx: xx: xx': {'nome do host': 'desconhecido',
                       'ipv4': '192.168.12.x',
                       'lastseen': '20150208-21: 06',
                       'ports': {53: 'domínio [tcp]',
                                 137: '[udp] netbios-ns',
                                 139: '[tcp] netbios-ssn',
                                 445: '[tcp] microsoft-ds',
                                 548: '[tcp] afp',
                                 5009: «[tcp] airport-admin»,
                                 5353: '[udp] zeroconf',
                                 10000: '[tcp] snet-sensor-mgmt'},
                       'status': 'up',
                       'type': 'Apple'},
 'xx: xx: xx: xx: xx: xx': {'nome do host': 'desconhecido',
                       'ipv4': '192.168.12.x',
                       'lastseen': '20150208-21: 06',
                       'ports': {5000: '[tcp] upnp', 5353: '[udp] zeroconf'},
                       'status': 'up',
                       'type': 'Apple'},
 'xx: xx: xx: xx: xx: xx': {'nome do host': 'desconhecido',
                       'ipv4': '192.168.12.x',
                       'lastseen': '20150208-21: 06',
                       'ports': {5000: '[tcp] upnp', 5353: '[udp] zeroconf'},
                       'status': 'up',
                       'type': 'Apple'}}
"" "

#obter informações do host local 
import re
uuid de import
socket import

IP da class:
   """Obtém os endereços IP e MAC do host local"""
   ip = 'x'
   mac = 'x'
   def _init(self):
       """ Tudo é feito em init(), não chame nenhum método, basta acessar ip ou mac"""
       user.mac = self.getHostMAC()
       user.ip = proprio.getHostIP()
    
    def gethostIP(self):
        """
        precisa obter o endereço IP do host loval
        em: nenhum
        out: retorna o endereço IP da maquina host
        """
        
        host_name = socket.getHostname()
        if '.local' não estiver em host_name : host_name =  host_name + 'local'
        ip = socket.gethostbyname(host_name)
        return ip
    def getHostMac(self):
        """
		A principal falha do NMAP não permite que você obtenha o endereço MAC do host local, portanto, esta é uma solução alternativa.
		em: nenhum
		out: string hexadecimal para o endereço MAC 'aa: bb: 11: 22 ..'
		"""
        return ':' .junção(re.findall('..', '%012x' % uuid.getnode()))

class NetworkScan:
    "" "O NetworkScan utiliza o Nmap para detectar hosts na rede e depois verificar suas portas." ""
    def _init_(self):
        user.this.host = IP()
        
    def nmap_cmd(user, tgt, cmd):
        """Ola"""
        nmap_proc = NmapProcess(destinos = tgt, opções = cmd)
        nmap-proc.run()
        xml_msg = nmap_proc.stdout
        nmap_report = NmapParser.analisae(xml-msg)
        return nmap_report
   
    
    def hetHostName(auto, ip):
        """Use as ferramentas avahi (zeroconfig) para encontrar um nome de host ... isso só funciona
		no Linux usando as ferramentas avahi.
	
		em: ip
		out: string com nome do host
		"""
        name = 'desconhecido'
        if _platform == 'linux' or _platform == 'linux2':
            cmd = ["avahi-resolve-address% s | awk '{print $ 2}'" %(ip)]
            #name = self.runProcess(cmd)
            nome = subprocesso.popen(cmd, stdout = subprocess.pipe, stderr = subprocess.pipe, shell = verdadeiro).communic() [0]
            nome = nome.rstrip()
            if nome == '' : nome = 'desconhecido'
        nome of return
    def ping(self, tgts):
       
        
        """Determine quais hosts estão em uma rede.
		in: tgts - qualquer endereço IP ou intervalo do nmap: 1.1.1.1/24 ou 1.1.1.1-25
		out: lista de endereços IP que responderam ao ping 
		
		nmap: 
			-sn desativar verificação de porta
			-P use portas específicas para determinar se um host está ativado ou não
			
		Portas comuns abrem nos meus computadores Apple para coisas
		SERVIÇO DO ESTADO DO PORTO
		22 / tcp ssh aberto
		88 / tcp aberto kerberos-sec
		548 / tcp afp aberto
		88 / udp aberto | Kerberos filtrados-sec
		123 / udp ntp aberto
		137 / udp open | netbios-ns filtrados
		138 / udp aberto | netbios-dgm filtrado
		5353 / udp open | zeroconf filtrado
		"""
        
        nmap_report = self.nma_cmd(tgts,"-sn 'PS22,80,88,123,443,548,5009,5353")
        hosts = nmap_report.anfitriões
        
        up = []
        for hosts in hosts:
            if hospedar.is_up():
                for upper.append(anfitrião, ID):
        back
        
        def portScan(auto, ip):
         """Examine as portas em um endereço IP específico.
		Opções:
		   Verificação de sincronização TCP -sS
		   -sU verificação UDP
		   -F verificação rápida
		""" 
        nmap_report = self nmap_cmd(ip, '-sS -sU -F')
        hosts = nmap_report. anfitriões
        for hosts in hosts:
            p = {}
            #print host.hostnames, host.id, host.mac, host.vendor, 'up:', host.is_up ()
            for serv no host.service:
             #print serv.port, serv.protocol, serv.service
				se  serv . open (): p [ str ( porta serv . )] = '[' + serv . protocolo + ']' + serv . serviço   
                
            val = {'ipv4' : ip, 'hostname' > 'unknowm', 'ports' : p, 'status' : 'up', 'type' : host.fornecedor}
            chave = hos.mac.upper() #faz letras maiusculas
        key of return, val
        
def canNetwork(proprio, liquido)
"""
		Função principal de scanner de rede.
		 1. encontre hosts
		 2. digitalize-os para portas abertas e endereço de HW
		 3. obtenha o nome do host (somente no linux)
		 4. retornar ditado de hosts, nome, ID, IP
	
		in: intervalo de ip da rede, por exemplo: 192.168.1.0/24
		out: dict com informações para cada sistema encontrado
		"""
        
        up = self.ping(liquido)
        pp.print(upper)
        hosts = dict()
        time_now = str(datetime.datetime.now().strftime('% Y% m% d-% H:% M' ))
        stop ip in up:
            if ip == : continue
        #print '[+] varredura de ip:', ip
        name = self.getHostName(ip)
        mac, info = self.portScan(ip)
        
        
        #tente novamente 
        if not for mac:
            if eu.this.host.ip == ip:
                mac = self.this_host.Mac
            for:
                print 'tente', ip, 'novamente'
                mac, info = self.portScan(ip)
            if mac == '' :
                print 'Error', ip
            for:
                info ['lastseen'] = time_now
                info ['hostname'] = nome
                hosts [mac] = informções
            return hosts
        
        def wol (auto, mac):
            """
		Wake-on-lan (wol)
		em: hw addr
		fora: nenhum
		"""
        wol.send_magic_packet(mac)
def main():
    n = networkScan()
    info = n.scanNetwork('192.168.1.1-5')
    pp.print(informações)
    
    if _name_ == '_main_':
        main()
        