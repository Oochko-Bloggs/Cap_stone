import socket 
import subprocess

def get_router_ip():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

router_ip = get_router_ip()
print("Router IP address: ", router_ip)
network_ip = '.'.join(router_ip.split(".")[0:3])
print(f'Network IP : {network_ip}')
result = subprocess.run(["./Ipaddr.sh",network_ip], capture_output=True)

connection_info = result.stdout.decode().splitlines()
connection_info.remove(router_ip)

print('\n'.join(connection_info))

