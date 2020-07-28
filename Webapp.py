 fila de import
 rosqueamento de importação
import  os
import  urllib2

threads    =  10 

target     =  "http://www.test.com"
directory  =  "/Users/justin/Downloads/joomla-3.1.1"
filtros    = [ ".jpg" , ".gif" , "png" , ".css" ]

os . chdir ( diretório )

web_paths  =  Fila . Fila ()

para  r , d , f  em  os . andar ( "." ):
    para  arquivos  em  f :
        remote_path  =  "% s /% s"  % ( r , arquivos )
        se  remote_path . começa com ( "." ):
            remote_path  =  remote_path [ 1 :]
        se  os . caminho . splitext ( arquivos ) [ 1 ] não  nos  filtros :
            web_paths . put ( remote_path )

def  test_remote ():
    enquanto  não  web_paths . vazio ():
        path  =  web_paths . get ()
        url  =  "% s% s"  % ( destino , caminho )

        request  =  urllib2 . Solicitação ( URL )

        tente :
            response  =  urllib2 . urlopen ( solicitação )
            conteúdo   =  resposta . read ()

            print  "[% d] =>% s"  % ( resposta . código , caminho )

            resposta . fechar ()
        
        exceto  urllib2 . HTTPError  como  erro :
            #print "Falha% s"% error.code
            passar
        
        

para  i  no  intervalo ( threads ):
    print  "Tópico desova:% d"  %  i
    t  =  rosca . Thread ( target = test_remote )
    t . start ()