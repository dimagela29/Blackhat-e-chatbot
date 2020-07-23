class PassiveMapper(object):
      def _init_(self):
        user.mpa = []
processo de def(self, hrd, data):
    """
    processa cada pacote de pcap
    """
eth = dpkt.ethernet.Ethernet(data)
a = auto.p.decodificar(eth)
if one:
    user.map.index(a)
    
def pcap(self, frame):
    """
    abre um arquivo pcap e le o conteudo
    """
    cap = pcapy.open_offline(fname)
    
    user.map = []
    use.p = PacketDecoder()
    cap.loop(0, auto.processo)
    return user.map
def rr(auto, rec):
    ans = {'nome do host' : '', 'tcp' : [], 'udp': []}
    for line in rec [ 'rr' ]:
        rtype = linha [ 'tipo' ]
        if rtype == 'ptr':
            pass
        elif rtype == 'txt':
            pass
        elif rtype == 'srv':
            ans [ 'hostname' ] = linha [ 'hostname' ]
            if linha [ 'proto' ] == '_tcp' : ans [ 'tcp' ].add({'srv': linha [ 'srv' ], 'porta' : linha [ 'porta' ]})
            elif linha [ 'proto' ] == '_udp' : ans [ 'udp' ].add({'srv': linha [ 'srv' ], 'porta' : linha [ 'porta' ]})
        add:
            print('Algo aconteceu', linha)
            
            #elif type == 'rr': print 'rr'
        elif rtype = 'aaaa':
            ans [ 'ipv6' ] = linha [ 'ipv6' ]
            ans [ 'hostname' ] = linha [ 'hostname' ]
            #ans [ 'mac' ] = linha [ 'mac' ]
            sum:
                print('Algo deu erraddo, tente novamnete', linha)
        if not ans [ 'hostname' ] and not ans [ 'tcp' ]:
            ans = {}
            return ans
filter definition(auto, rec):
    """
    a saida do pcap é apenas uma lista de registros, isso condensa/combina
    as informções em um mapeamento da rede.
    """
    
    ans = []
    for line in rec:
        if 'rr' na linha:
            # print 'rr:', linha ['rr']
				# print 'mdns'
                a = auto.rr(linha)
                if one:
                    a ['type'] = 'rr'
                    ans.extend(a)
        elif 'type' na linha:
            #linha de impressão ['type']
            rtype = linha [ 'tipo' ]
            if type == 'ptr': print 'ptr'
        elif type == 'txt': print 'txt'
        if rtype == 'aaaa': ans.insert(linha)
        elif rtype == 'a': ans.insert(linha)
        elif rtype == 'arp': ans.insert(linha)
        else:print('<<<<' 'linha', '>>>>' )
        add:
            print('******', 'linha', '******')
def find(self, a, b):
    if 'IPv4' for in i e 'IPv4' em um:
        if user [ 'ipv4' ] == a [ 'ipv6' ]:
            i.atualização(a)
            return
        elif 'hostname' for in e 'hostname' range:
            if e [ 'hostname' ] == a [ 'hostname' ]:
                i.atualização(a)
                return
b.index(a)
return

def combine(self, nmap):
    """
    muito a fazer
    """
    ans = []
    for host no nmap:
        user.localizar(host, ans)
        return ans
    def live(self, dev, loop = 500):
        """
        dispositivo aberto
        os argumentos aqui são:
            dispositivos
            snaplen(numero máximo de bytes para capturar _per_packet_)
            modo promiscuo(1 para true), precisa false para OSX
            tempo limite em milisegundos
            """
            #verifique os privilegios  sudo / root
            if os.getuserid() != 0:
                exit('Voce precisa ser root / sudo para sair em tempo real...')
                
            #tempo real
            cap = pcapy.open_live(dev, 2048, False, 50)
            
            #cap setfilter(udp)
            
            user.map = []
            user.p = PacketDecoder()
            
            # comeca pesquisar pacotes
            while(loop):
                exec:
                    loop -= 1
                    (cabeçalho, dados) = proximo(limit)
                except KeyboardInterrupt:
                    print('Voce pressiona ^C, saindo do passiveMapper... Tchau')
                    exit()
                except:
                    continue
                user.process(cabeçalho, dados)
            return user.map
        break
    finish
    