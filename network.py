import socket

def get_local_info():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return {"hostname": hostname, "local_ip": local_ip}