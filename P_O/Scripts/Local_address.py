import socket 
import subprocess

def get_router_ip():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

def info():
    router_ip = get_router_ip()
    print(f"Your IP address : {router_ip}")
    network_ip = '.'.join(router_ip.split(".")[0:3])
    print(f'Network IP : {network_ip}')
    result = subprocess.run(["./ip_sweeper.sh",network_ip], capture_output=True)

    connection_info = result.stdout.decode().splitlines()
    connection_info.remove(router_ip)
    
    for index,addr in enumerate(connection_info):
        print(f'{index}\t......{addr}')
    return connection_info


if __name__ == '__main__':
    info()
