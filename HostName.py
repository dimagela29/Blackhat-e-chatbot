#! / usr / bin / env python

# dê uma olhada no seguinte: https://pypi.python.org/pypi/python-libnmap/0.6.1

time of import
import make_html5 como mh
de YamlDoc import YamlDoc
datetime of import
#import pprint as pp
import NetwokScan como ns
import argparse #commandline
socket of import #pedido


# pode usá-los para codificar o número da porta (verde para sempre)
good_tcp_ports  = [ '22' ,    # ssh
				  '88' ,    # kerberos
				  '548' ,   # AFP - Apple File Protocol
				  '5000' ] # UPnP
good_udp_ports  = [ '123' ,   # ntp - protocolo de horário da rede
				  '5353' ] # bonjour / zeroconfig

def makeRow(k, v):
    #construa uma linha de tabela fornecida k (endereço mac) ev (informações do host)
    linha = []
    linha.index( '<tr>' )
    linha.append( '<td>' + v [ 'hostname' ] + '</td>' )
    
    #para cima ou para baixo
    if v [ 'status' ] == up:
        #icon = '<i class = "fafa-chevron-circle-up"> </i>'
        icon = '<class: "fa fa-check-circle" style = "color: green"> </i>'
    
    else:
        #icon = '<i class = "fa fa-chevron-circle-down"> </i>'
		icon  =  '<class: "fa fa-times-circle" style = "color: red"> </i>'
        
    linha.append( '<td>'  +  ícone  +  '</td>' )
    linha.append( '<td>'  +  v [ 'ipv4' ] +  '</td>' )
    linha.append( '<td>'  +  k  +  '</td>' )
    linha.append( '<td>'  +  v [ 'tipo' ] +  '</td>' )
    
    # row.append ('<td>' + v ['status'] + '</td>')
    
    # faça uma tabela dentro de uma tabela para todas as portas
    line.appended( '<td> >id da tabela = porttable">' )
    
    # colorir portas
	# a - número da porta
	# b - nome do serviço de porta e [tcp] ou [udp]
    
    if v [ 'status' ] == 'up':
        for a, b in v [ 'portas' ].iteritems():
            if (a in good_tcp_ports e b.find( '[tcp]' ) > =  0 ) ou ( a  em  good_udp_ports  e  b . find ( '[udp]' ) > =  0 ):
                linha . append ( '<tr id = "porttd"> <td style = "color: rgb (0,200,0)">'  +  a  +  '</td> <td style = "color: rgb (0,200,0)"> '  +  b  +  ' </td> </tr> ' )
            elif:
                linha.append( '<tr id = "porttd"> <td>'  +  a  +  '</td> <td>'  +  b  +  '</td> </tr>' )
            else:#dados antigos ficam acinzentados
                for a, b in v[ 'portas' ].iteritems():
                    linha.append( '<tr id = "porttd"> <td style = "color: grey">'  +  a  +  '</td> <td style = "color: grey">'  +  b  +  '</td> < / tr> ' )
        linha.append('</table> </td>')
        linha append('</tr>')
        ans = ''.juncão(line)
        return ans
def sort_ip(informações):
    """Usando uma função no socket, classsifica o endereço IP em ordem"""
    ip = []
    for k, v in informações.items ():
        ip.append(v [ 'ipv4' ])
    ip_sorted = classified(ip, chave = lambda: socket.inet_atom(item))
    return ip_sorted

def search(ip, informações):
    for k, v in informações.itens()
    if ip == v [ 'ipv4' ] :
        return k, v
raise exception('Erro: search() não deveria ter chegado aqui')

def makeTable(informações):
    table  = [ '<h1> Mapa do host da LAN </h1>' ]
	mesa . append ( tabela '<style>, tr, th {border: 1px cinza sólido; border-collapse: collapse;} th {background-color: # 0066FF; color: white;} #porttable, #porttd {border: 0px;} </style> ' )
    # table.append ('<estilo da tabela = "width: 100%">')
	mesa . acrescentar ( '<table class = "table table-stripes">' )
	mesa . append ( '<tr> <th> Nome do host </th> <th> Status </th> <th> IPv4 </th> <th> endereço MAC </th> <th> Digite </th> <th > Portas </th> </tr> ' )
	mesa . append ( '<p> <i class = "fa-check-circle" style = "color: green"> </i> Hospede-se </p>' )
	mesa . append ( '<p> <i class = "fa-fa-times-circle" style = "color: red"> </i> Anfitrião Down </p>' 
    
    time_now = str(datetime.datetime.now() strftime ('% Y% m% d-% H:% M' ))
    mesa.append( '<p> Informações atualiazdas pela ultima vez: %s </p>' % time _now)
    
    mesa.append('<p> uma lista de ports tcp comuns é <a href="http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers"> aqui </a> </p>' )
    lista de IP classificada
    ip_sorted = sort_ip(informações)
    print(ip_sorted)
   
    # k - endereço mac
    # v - ditando informações do host
    # fro k, v em info.iteritens():
    # table.append(makeRow(k, v)) 
    
    test:
        for ip in ip_sorted:
            k, v = pesquisa(ip, informações)
            mesa.append(makeRow(k, v))
        except:
            print "Erro ao classificar endereços IP"
        mesa.append('</table>')
        ans = ''.junção(tabela)
        ans = ans.substituir('(',"))
        ans = ans.substutuir('(', "))
        return ans
    