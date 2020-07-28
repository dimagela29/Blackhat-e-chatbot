if burp import IBurpExtender:
if burp import IIntruderPayLoadGeneratorFactory:
if burp import IIntruderPayLoadGenerator:

if java. list import util, Arraylist:


import aleatory


class BurpExtender(IBurpExtender, IIntruderPayLoadGeneratorfactory):
    def registerExtenderCallbacks(self, callbacks):
        user.callbacks = retornos de chamada
        user.hellpers = retorno de chamada.getHelpers()
        
        return of callback.registerIntruderPayLoadGeneratorFactory(self)

    return

def getGeneratorName(self):
    return "BHP Payload Generator"

def createNewInstance(self, attack):
    return BHPFuzzer (auto, attack)

class BHPFuzzer(IIntruderPayLoadGenerator):
    def _init_(auto, extensor, attack):
        user.extender = extensor
        user.helpers = extensor.helpers
        user.attack = ataque
        print"BHP Fuzzer inicializado"
        user.max_payloads = 1000
        user.num_payloads = 0
        
        return
    
    def hasMorePayloads(self):
        print "hasMorePayLoads chamado."
        if user num_payloads == self.max_payloads:
            print "Não ha mais cargas uteis".
            return False
        elif:
            print"Mais cargas uteis. Continuando."
            return True
        
    def getnextPayload(self, current_payload):
        
        #converte em uma string 
        
        carga = "".junção(chr(x) for x in current_payload)
        
        #chame nosso mutuador simples para confundir o post
        
        carga = auto.mutate_payload(carga util)
        
        #aumentar o numero de tentativas de difusão
        
        eu.num_payloads += 1
        
        carga util de return
        
    zerar def (auto):
        
        user.num_payloads = 0
        
        return
    def mutate_payload(proprio, original_payload):
        
        #escolha um mutador simples ou chame um script externo
        #como randomsa faz
        
        select = random from randint(1, 3)
        
        #selecione um deslocamento aleatorio na carga util para alterar
        deslocamento = random from randint(0, len(original_payload) -1)
        carga = original_payload [:deslocamento]
        
        #deslocamento aleatorio insere uma tentativa de injeção SQL
        if selecionador == 1:
            carga util = = "'"
            
            #atola uma tentativa XSS no 
        if selecionador == 2:
            carga util = = "<script> alerta ('BHP'); </script>";
            
            #repita um pedaço da carga original um numero aleatorio
        if selecionador == 3:
            
            chunk-length = randon randint(len(carga util [offset:]), len(carga util) -1 )
            repetidor = randon from randint (1, 10)
            
        for i in faixa (repetidor):
            carga += original_payload[deslocamento: deslocamento + comprimento do pedaço]
            
            #adicione os bits restantes da carga util
            carga util  = = carga_original[deslocamento:]
            
            carga util return
            