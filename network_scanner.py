import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)
    
scan("192.168.112.1/24")