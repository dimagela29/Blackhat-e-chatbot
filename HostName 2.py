#!/usr/bin/env python3
# "" "
# Função simples para comer espaço em branco duplicado
# 'oi, tudo bem' -> 'oi, tudo bem'
# in: string com espaço em branco extra
# out: string com espaço em branco extra removido
# "" "
# def killws (str):
# return re.sub ('+', '', str)

"""
Banco de dados simples que abstrai como eu armazeno informações do host. O atual
a configuração é assim:
58: b0: 35: f2: 25: d8:
  nome do host: 'desconhecido'
  ip: 192.168.1.4
  Última atualização: 20141130-21: 01
  status: up
  tcp: {'22': ssh, '548': afp, '88': kerberos-sec}
Poderia mudar para um banco de dados real, mas minha rede é pequena e um arquivo simples funciona bem.
"""
banco de dados da class :
    def _int_(self):
        user.db = dict()
     
    def load(nome usuario, nome arquivo):
        y = YamlDoc()
        user.db = y.read(nome do arquivo)
        if (self.db)!= dict:
            user.db = dict()
    
    def save(nome usuario, nome arquivo):
        y = Yamldoc()
        y.write(nome do arquivo, self,db)
        
        
	"""
	Dados os novos resultados da verificação, isso marca primeiro todos os hosts inativos e, quando atualizados, eles são marcados.
	em: ditado de informações do host
	fora: nenhum
	"""	
    
    atualização de definição(auto, lista)
    for k, v in user.db.itens():
        v ['status'] = 'inativo'
        
    for k, v in list.itens():
         #isso é meio desleixado, consertar?
	     # é o endereço mac no banco de dados? sim
    if k in user.db:
        hostname = user.db [k]
        user.db [k] = v
        
        if hostname != 'desconhecido' e user.db [k] ['hostname'] == 'desconhecido':
            user.db [k] = nome do host
            #não então apenas pegue o que tivermos 
    elif:
        user.db [k] = v
    
def diff(auto, lista):
    return 0, dict()

def hw_addr(proprio):
    ans = list()
    for k in user.db:
        ans.append(k)
    return ans

def getDict(self):
    out = user.db
    return out

"" "
Enviar notificação por SMS
in: message
fora: nenhum
"" "
def  notify ( itens ):
	retornar  0	

def  make_webpage ( informações , HTML_FILE ):
	tabela  =  makeTable ( informações )
	página  =  mh . Página da Web ()
	página . create ( tabela , 'Mapa do host da LAN' )
	página . savePage ( HTML_FILE )

def  handleArgs ():
	analisador  =  argparse . ArgumentParser ( 'Um simples programa de reconhecimento de rede usando o nmap que cria uma página da web.' )
	analisador . add_argument ( '-p' , '--page' , help = 'nome da página da web' , padrão = './network.html' )
	analisador . add_argument ( '-n' , '--network' , help = 'rede para varredura: 10.1.1.0/24 ou 10.1.1.1-10' , padrão = '192.168.1.0/24' )
	analisador . add_argument ( '-y' , '--yaml' , help = 'arquivo yaml para armazenar a rede em' , padrão = './network.yaml' )
	analisador . add_argument ( '-s' , '--sleep' , help = 'quanto tempo de espera entre as verificações' , padrão = 3600 )
	
	args  =  vars ( parser . parse_args ())
	
	retornar  argumentos
    
def main ():
    args = hanldeArgs()
    YAML_FILE = str(args['yaml'])
    NETWORK  str(args[rede])
    SLEEP = int(args['sono'])
    WEBPAGE = args['pagina']
    
    db = banco de dados()
    db.carregar (YAML_FILE)
    
    scan = ns.NetworkScan()
    
    for 1:
        # acordar as coisas
		hw_addr  =  db . hw_addr ()
		para  mac  em  hw_addr :
			digitalizar . wol ( mac )
		
		imprima  '*' * 10 , 'Iniciar digitalização em' , REDE , '*' * 10
		lista  =  varredura . scanNetwork ( REDE )
		# pp.pprint (lista)
		
		# ans, new_items = db.diff (lista)
		db . atualização ( lista )
		
		#if ans == true:
		# notify (new_items)
		
		print  '>> Salvar:' , YAML_FILE , '<<'
		db . salvar ( YAML_FILE )
		
		print  '>> Write:' , WEBPAGE , '<<'
		make_webpage ( db . getDict (), WEBPAGE )
		
		hora . sono ( SLEEP )
        
    if _name_ == '_main'_:
        main()
        
    