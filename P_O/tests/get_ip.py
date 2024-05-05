import socket 

def get_router_ip():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

router_ip = get_router_ip()
print("Router IP address: ", router_ip)
