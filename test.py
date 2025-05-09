from scapy.all import IP, TCP, send

ip = "192.168.1.100"  
port =80


packet = IP(dst=ip) / TCP(dport=port, flags="S")



send(packet, loop=1, count=100)  

