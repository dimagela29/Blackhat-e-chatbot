def client_sender(buffer):
    cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try: 
    #conecta-se ap nosso host-alvo
    client.connect((target, port))
    if len(buffer):
        client.send(buffer)
        while True:
    #esperar receber dados de volta
    recv_len = 1
    response = ""
    
while recv_len:
    data = client.recv(4096)
    recv_len = len(data)
    response+= data
    if recv_len <4096:
        break
    print response,
    #espera mais dados de entrada 
    buffer = raw_input("")
    buffer += "\n"
    
    #envia os dados 
    client.send(buffer)
    except:
print("[*] Exxeption! Exiting."
#encerra a conexão
client.close()

def server_loop():
    global target
    #se não houver nenhum alvo definido ouviremos todas as interfaces
    if not len(target):
        target = "0.0.0.0"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((target, port))
server.list(5)

while True:
    client_socket,addr = server,accept()
#dispara uma thread para cuidar do nosso novo cliente 
    client_thread =  threading.Thread(target=client_handler, args=(client_socket,))
client_thread.start()
def run_command(command)
#remove a quebra de linha
command =command.rsttrip()

#executa o comando e obtem os dados de saida
try:
    output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=true 
except:
    output = "Failed to execute comand.\r\n"
    #envia os dados de saida de volta ao cliente
    
    return output

def client_handler(client_socket):
    global upload
    global execute 
    global command
    
    #verifica se é upload
    if len(upload_destination):
#le todos os bytes e grava em nosso destino
        file_buffer = ""
        
        #permanece lendo os dados até que não haja mais nenhum disponivel
        while True:
            data =client_socket.recv(1024)
            
            if not data:
                break
            else:
                file_buffer +=data
                
                #agora tentaremos gravar os bytes 
                try:
                    file _descriptor = open(upload_destination,"wb")
                    file_descriptor.write(file_buffer)
                    file.descriptor.clos()
                    
                    #confirma que gravamos o arquivo
                    client_socket.send("Sucessfully saved file to %s\r\n" % upload_destination)
                    except:
                        client_socket.send("Failed to save file to %s\r\n" % upload_destination)
                        #verifica se e execução de comando
                        if len(execute):
                            #executa o comando
                            output = run_command(execute)
                            client_socket.send(output)
                    #entra em outro laço se um shell de comandos foi solicitado
                    if command:
                        while true:
                            #Mostra um prompt simples
                            client_socket.send("<BHP:#> ")
                                
                                #Agora ficamos recebendo os dados ate vermos um linefeed
                                cmd_buffer = ""
                                while "\n" not in cmd_buffer:
                                    cmd_buffer += client.socket.recb(1024)
                                    
                                    #envia de volta a saida do comando
                                    response = rum_command(cmd_buffer)
                                    
                                    #envia de volta a resposta
                                    clien+socket.send(response)
                                    
                                