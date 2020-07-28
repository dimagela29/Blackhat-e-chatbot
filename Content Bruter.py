import urllib2
import urllib
socket import
file import

threads       = 5
target_url    = "https://testphp.vulnweb.com"
wordlist_file = "/tmp/all.txt" #do SVNDigger
resume        = None
user_agent    = "Mozzila / 5.0 (x11; linux x86_64; rv: 19.0) Gecko / 20200101 firefox / 19.0"

def build_wordlist(archive of list de palavras):
    
    #ler na lista de palavras
    fd = aberto(wordlist_file, "rb")
    raw_words = fd.readlines()
    fd.exit()
    
    found_resume = False
    words        = Queue.file()
    
    for palavras in raw_words:
        
        palavra = palavra.rstrip()
        
        if resumo not range Nenhum:
            if found_resume:
                palavras.colocar(palavra)
            
            elif:
                if word == resume:
                    found_resume = True
                    print"Reiniciando a lista de palavras de :%s" % resume
                    
        elif:
            palavras.colocar(palavras)
    
    return palavras
    
def dir_bruter (extensio = Nenhuma):
    while not Word_queue.vazio():
        test = file of wordpress.get()
        
        try_list = []
        
        #verifique se ha uma extensão de arquivo se não houver 
        #é um caminho de diretorio que estamos brutando
        
        if "." not in test:
            try_list.insert("/% s/" % tentativa)
        
        elif:
            try_list.insert("/% s" % tentativa)
            
        #se quisermos usar extensões de força bruta 
        
        if extensions:
            if extension in extensions:
                try_list.insert("/% s% s" % (tentativa, extension))
        #iterar sobre nossa lista de tentativas
        
        for bruto in try_list:
            
            url = "% s% s" % (target_url, urllib.aspas(bruto))
            
            test:
                cabeçalhos = {}
                cabeçalhos ['User-Agent'] = user_agent
                r = urllib2.solicitação(url, headers = headers)
                
                response = urllib2.urlopen(r)
                
                if len(response.leia()):
                     print  "[% d] =>% s"  % ( resposta . código , url )
        
    except urllib2.HTTPError, e:
        
        if e.code != 404:
            print"!!!% d =>% s"  % ( e . código , url )
        pass
word_queue  =  build_wordlist ( arquivo de lista de palavras )
extensões  = [ ".php" , ".bak" , ".orig" , ".inc" ]

for i in intervalo(threads):
    t = socket.thread(target = dir_bruter, args = (extensions))
    t.start()
    