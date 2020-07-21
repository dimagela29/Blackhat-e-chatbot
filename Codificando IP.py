import socket

import os 
import struct
from ctypes import *
#host que ouvira
host = "192.168.0.187"

#nosso cabecalho ip
class IP(Structure):
    _fields_ = [
        ("ihl",    c_ubyte, 4)
        ("version",c_ubyte, 4)
        ("tos",    c_ubyte)
        ("len",    c_ushort)
        ("id",     c_ushort)
        ("offset", c_ushort)
        ("ttl",    c_ubyte)
        ("protocol_num", c_ubyte)
        ("sum",    c_ushort)
        ("src",    c_ulong)
        ("dst",    c_ulong)
        ]
    def _new_(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)
    def_init_(self, socket_buffer=None):
        
#mapeia constantes do protocolo aos seus nomes
        self.protocol_map = {1:"ICMP", 6:"TCP",17:"UDP"}
        
        # endereços IP legiveis aos seres humanos 
        self.src_adress = socket.inet_ntoa(struct.pack("<L" ,self.src))
        self.dst_adress = socket.inet_ntoa(struct.pack("<L" ,self.dst))
        
        #protocolo legivel aos seres humanos 
        try: 
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            sel.protocol = str(self.protocol_num)
    #este codigo e igual o anterior
    
    
            