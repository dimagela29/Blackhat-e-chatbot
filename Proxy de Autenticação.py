import sys 
import socket
import threading
def server_loop(local_host,local_port,remote_host,remote_port,received_first):
    server = socket.socket(socket.´AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(local_host,local_port)
        except:
            print"[!!] Failed to listen on %s:%d" % (local_host,local_port)
            server.listen(5)
            while True:
                client_socket,addr = server.accept()
                
                #exibe informações sobre a conexão local
                print"[===>] Received incoming connection from %s:%d" % (addr[0], addr[1])
                
                #inicia uma thread para conversar com host remoto
                proxy_thread =threading.Thread(target=proxy,handler,
                                               args=(client_socket,remote_host,remote_port,receive_first))
                proxy_thread.start()
                
        def main():
                    #sem parsing sofisticado de linha de comando nesse caso
                    if len(sys.argv[1:]) != 5:
                        print "Usage: ./proxy.py[localhost] [localport] [remotehost] [remoteport] [received_first]"
                        print: "Example: ./proxy.py127.0.0.1 9000 10.12.132.1 9000 True"
                        sys.exit(0)
        
#define parametros para ouvir localmente
local_host = sys.argv[1]
local_port = int(sys.argv[2])

#define o alvo remoto
remote_host = sys.argv[3]
remote_port = int(sys.argv[4])

#o codigo a seguir diz ao nosso proxy para conectar e receber dados
#antes de enviar ao host remoto
receive_first = sys.argv[5]
if True in receive_first:
    receive_first = True
else:
    receive_first = False
    # agora coloca em ação o nosso socket que ficara ouvindo
    server_loop(local_host, local_port,remote_host, remote_port, receive_first)
main()

def proxy_handler(cliente_socket, remote_host, remote_port, receive_first):
    #conecta-se ao ohost remoto
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.conncet((remote_host,remote_port))
    
    #recebe dados do lado remoto, se for necessário
    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)
        
        #envia os dados ao handler de resposta 
        remote_buffer = response_handler(remote_buffer)
        #se houver dados para serem enviados ao nosso cliente local envia-os 
        if len(remote_buffer):
            print"[<===] Sending %d bytes to localhost." %
            len(remote_buffer)
            client.socket.send(remote_buffer)
            #agora vamos entrar no laço e ler do host local
            #enviar para o host remoto, enviar para o host local,
            #enxaguar lavar e repetir
            while True:
                # le do local host
                local_buffer = receive-from(client_socket)
                
                if len(local_buffer):
                    print"[===>] received %d bytes from local host" % len(local_buffer)
                    hexdump(local_buffer)
                   
                    #envia os dados para nosso handler de solicitações
                    local_buffer = request_handler(local_buffer)
                    
                    #envia os dados ao host remoto
                    remote_socket.send(local_buffer)
                    print"[===>] sent to remote"
                    
                    #recebe a resposta
                    remote_buffer = receive_from(remote_socket)
                    
                    if len(remote_buffer):
                        print"[<===] received %d bytes from remote." % lne(remote_buffer)
                        hexdump(remote_buffer)
                        
                        #envia os dados ao nosso handler de resposta
                        remote_buffer = response_handler(remote_buffer)
                        
                        #envia a resposta para o socket local 
                        client_socket.send(remote_buffer)
                        
                        print"[<===] Sent to localhost"
                        
                        #se não tiver mais dados em nenhum dos lados encerra as conexões
                        if not len(local_buffer) or not len(remote_buffer):
                            client_socket.close()
                            remote_socket.close()
                            print"[*]No more data. Closing connections."
                            
                            break
                        
