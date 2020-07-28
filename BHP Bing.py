in burp import IburpExtender
in burp import IContextMenuFactory

in javax import swing JmenuItem
in java list if import util, Arraylist
in java Url import liquida

socket import 
import urllib
import json
import re
import base64

bing_api_key = "USERKEYHERE"

class BurpExtender(IBurpExtender, IContextMenuFactory):
    def registerExtenderCallBacks (self, callbacks):
        user.callbacks = return callbacks
        user.helpers = return callbacks.getHelpers()
        user.context = None 
        
        #montamos nossa extensão
        
        return callback.setExtensionName(BHP Bing)
        return callback.registerContextMenuFactory(self)
    return

    def createMenuItems(self, context_menu):
        user.context = context_menu
        menu_list = ArrayList ()
        menu_list.add (JmenuItem("Enviar para o Bing", actionPerformed = self.bing_menu))
        
        return menu_list
    def bing_menu (proprio, event):
       
        #pegue os detalhes do que o usuario clicou
        http_traffic = self.context.getSelectMessages()
        
        print "% d solicitações destacadas" % len(http_traffic)
        
        for traffic in http_traffic:
            http_service = traffic.getHttpService()
            host         = http_service.gethost()
            
            print"Host selecionado pelo usuário: %s" % host
            
            user.bing_search(host)
            
            return
        def bing_search(auto, host):
            
            #verificamos se temos um ip ou nome de host
            
            is_ip = re.match("[0-9] +(?:\.[0-9]+) {3}", host
        
        if is_ip:
            ip_adress = host
            domain = false
       
        elif:
            endereço_ip = socket.gethostbyname(host)
            domain = true
            
        bing_query_string ="'ip:%s'" % endereço_ip
        user.bing_query(bing_query_string)
        
        if dominio:
            bimg_query_string = "'dominio:%s'" % host
            user.bing_query(bing_query_string)
            
        def bing_query(auto,bing_query_string):
            print('Executando a pesquisa do Bing:%s" % bing_query_string
                  
        #codifique nossa consulta
        quoted_query = urllib.citação(bing_query_string)
        
         http_request   =  "GET https://api.datamarket.azure.com/Bing/Search/Web?$format=json&$top=20&Query=%s HTTP / 1.1 \ r \ n "  %  quoted_query    
    http_request  + =  "Host: api.datamarket.azure.com \ r \ n "
    http_request  + =  "Conexão: fechar \ r \ n "
    http_request  + =  "Autorização:% s \ r \ n "  %  base64 básica . b64encode ( ":% s"  %  bing_api_key )
    http_request  + =  "Agente do usuário: Blackhat Python \ r \ n \ r \ n "
    
    json_body = self. _callbacks.makehttpRequest("api.datamarket.azure.com", 443, True, http_request). to string()
    json_body = json_body.division ("\r\n\r\n", 1) [1]
    
    test:
        r = json.cargas(json_body)
        if len (r ["d"] ["resultados"]):
            for site in r ["d"] ["resultados"]:
                
        print "*" * 100
        site of print['Titulo']
        site of print['URL']
        site of print['Descrição']
        print "*" * 100
        
        j_url = URL (site['Url'])
        
        if not user. _callbacks.isInScope(j_url):
            print"Adicionando ao escopo Burp"
            user. _callbacks.includeInScope(j-url)
except:
    print"Nenhum resultado do Bing"
    pass

return

        