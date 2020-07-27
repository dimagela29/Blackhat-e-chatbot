#! / usr / bin / env python

de __future__ import  print_function
importar  pcapy
# import os
 sys de import
 subprocesso de import # use commandline
 pedidos de import # whois
import  re
de  netaddr  import  valid_ipv4 , valid_mac
import  os
# import platform # socket alternativa para obter o nome do host
 socket de import
 

sudo tcpdump -s 0 -i en1 -w test.pcap
-s 0 definirá o byte de captura para seu máximo, ou seja, 65535 e não truncará
-i en1 captura a interface Ethernet
-w test.pcap criará esse arquivo pcap
tcpdump -qns 0 -X -r osx.pcap
$ sudo tcpdump -w osx.pcap
tcpdump: tipo de link de dados PKTAP
tcpdump: escutando no pktap, PKTAP do tipo link (Tapet Tap), tamanho da captura 65535 bytes
^ Pacotes C4414 capturados
4416 pacotes recebidos pelo filtro
0 pacotes descartados pelo kernel

def checksudo():
    return os.getuserid () == 0

def command(cmd):
ans = subprocess.popen([cmd], stdout = subprocesso.PIPE, stderr = subprocesso.PIPE, shell = True) .communicate () [0]
return ans

command of class(object):
    """ infelizmente os comandos extremamente simples/ uteis foram depreciados a favor do 
    subprocesso complexo/confuso... isso visa simplificar"""
    
    command def(self, cmd):
        ans = subprocess.popen ([cmd],stdout = subprocess.pipe, stderr = subprocess.pipe, shell = verdadeiro).communic () [0]
        return ans
    
class WhoIs(object):
    """ atualizada"""
    record = {}
    
    def _init_(auto, ip):
        if not for valid_ipv4(ip):
            print('Erro: o endereço de IPv4 {} é inválido'.format(ip))
            return
        rec = pedidos.get('http://whois.arin.net/rest/ip/{}.txt' .format(ip))
        if rec.status_code != 200:
            print('Erro')
            return
        ans = {}
        r = re.compile(r"/s/s+")
        b = rec.text.divide('/n')
        for l in b:
            if l and l [0] != '#':
            l = r.sub('',l)
            a = l.divide(':')
            
            ans [a[0]] = a [1]
        user.record = ans
        user.CIDR = ans ['CIDR']
        user.NetName = ans ['Netname']
        user.NetRange = ans ['NetRange']
        user.organização = ans ['Organização']
        user.atualizado = ans ['Atualizado']
        
class GetHostName (command):
    name = None
    def _init_(auto,ip):
        """ use as ferramentas avahi (zeroconfig) ou cavar para encontrar um nome do host 
        endereço de ip"""
        #lidar com endereço IP invalido
        
        if not for valid_ipv4(ip):
            print('O endereço IPv4 {} é inválido'.format(ip))
            return
        #manipular um endereço ip do host local
        if ip == '127.0.0.1' ou ip == 'localhost':
            self.name = platform.node()
            user.nome = socket.gethostname()
            return
        
        #agora fica complexo
        name = 'desconhecido'
        if sys.plataforma == 'linux' ou sy. plataforma == 'linux2':
            name = self.command("avahi-resolve-address{}|awk'{print$2}'".format(ip)), rstrip().rstrip('.')
        elif sys.plataforma == 'darwin':
            name = self.command('dig + short -x {} -p 5353 @ 224.0.0.251'.format(ip)).rstrip, rstrip('.')
            
            
            #detectar qualquer erro restante
            if nome.find('conexão excedeu o tempo limite') > = 0:
                name = 'desconhecido'
                
            user.name = nome
            
            #def cmdLine(proprio, cmd)
            #return subprocess.Popen([cmd], stdout = subprocess.PIPE, stderr = subprocess.pipe, shell = true).communicate() [0]
            
            class CapturePackets(object):
                """ Façam"""
                
        def _int_(self, iface, nome do arquivo = 'test.pcap', pcfilter = None, num_packets = 3000):
            #lista todos os dispositivos de rede
            #print pcapy.findalldevs()
            
            max_bytes = 1024
            promiscuo = false
            read_timeout = 100 # em milisegundos
            pc = pcapy.open_live(iface, max_bytes, promiscuo, read_timeout)
            if pcFilter: pc.setfilter(pcfilter)
            user.descarregador = pc.dump_open(nome do arquivo)
            pc.loop(num_packets, self.recv_pkts) #pacotes de captura
            
            #retorno de chamada para pacotes recebidos 
            def rec_pkts(seçf,hdr, data):
                except KeyboardInterrupt: #provalmente mostra erro de lançamento
                    exit('Saida do teclado')
                except:
                    exit("ALgo deu errado')
            
            def run (auto):
                pass
              # max_bytes = 1024
        # promiscuous = False
        # read_timeout = 100 # em milissegundos
        # pc = pcapy.open_live (iface, max_bytes, promíscuo, read_timeout)
        # if filter: pc.setfilter (filtro)
        # self.dumper = pc.dump_open (nome do arquivo)
        # pc.loop (num_packets, self.recv_pkts) # pacotes de captura
        
class maclookup(object):
    def _init_ (self, mac, full = false):
        user.vendedor= proprio.get(mac, completo)
    
    def get (self, mac, completo):
         "" "
        resposta json de www.macvendorlookup.com:
        {u'addressL1 ': u'1 Loop Infinito',
        u'addressL2 ': u' ',
        u'addressL3 ': u'Cupertino CA 95014',
        u'empresa ': u'Apple',
        u'country ': ESTADOS UNIDOS',
        u'endDec ': u'202412195315711',
        u'endHex ': u'B817C2FFFFFF',
        u'startDec ': u'202412178538496',
        u'startHex ': u'B817C2000000',
        u'type ': u'MA-L'}
        "" "
        desconhecido  = { 'empresa' : 'desconhecido' }
        
        if not for valid_mac(mac):
            print('Erro: O endereço Mac {} não é válido'.format(mac))
            return
        
        test:
            r = pedidos.get('http://www.macvendorlookup.com/api/v2/' + mac)
        except solicitações.exceções. HTTPError como e:
            print("httperror:", e .mensagem)
            return desconhecido
        
        if r status_code == 204: #nenhum conteudo encontrado, endereço mac incorreto
            print('Erro: Endereço MAC incorreto:', mac)
            return desconhecido
        
        a = {}
        test:
            se cheio: a = r.json() [0]
            add: a ['company'] = r.json () [0] ['empresa']
        except:
            print( 'ERRO:' , r . status_code , r . cabeçalhos , r . ok , r . texto , r . razão )
            a  =  desconhecido
            
            return um
        