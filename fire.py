from scapy.all import sniff, IP, TCP
from collections import defaultdict
from threading import Timer
import logging
import time
import csv
import subprocess

# Logging setup
logging.basicConfig(filename='dos_alerts.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

ip_counter = defaultdict(int)
THRESHOLD = 100
INTERVAL = 10
WHITELIST = {"127.0.0.1"}

# Save stats to CSV
def save_stats():
    with open("packet_stats.csv", "a", newline='') as f:
        writer = csv.writer(f)
        for ip, count in ip_counter.items():
            writer.writerow([time.ctime(), ip, count])

def detect_dos():
    print(f"\n[{time.ctime()}] Checking for DoS attacks... Total IPs: {len(ip_counter)}")
    save_stats()
    for ip, count in ip_counter.items():
        if ip in WHITELIST:
            continue
        if count > THRESHOLD:
            alert_msg = f"[!] Potential DoS attack from IP: {ip} - SYN Packets: {count}"
            print(alert_msg)
            logging.info(alert_msg)
            # Optional: block the IP using iptables
            # subprocess.call(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
    ip_counter.clear()
    Timer(INTERVAL, detect_dos).start()

def process_packet(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        tcp_layer = packet[TCP]
        if tcp_layer.flags == "S":  # SYN packet
            src_ip = packet[IP].src
            if not src_ip.startswith("127.") and src_ip not in WHITELIST:
                ip_counter[src_ip] += 1
                print(f"[+] SYN Packet from {src_ip}")

if __name__ == "__main__":
    print("Starting DoS detection firewall...")
    detect_dos()
    sniff(filter="tcp", prn=process_packet, store=0)

