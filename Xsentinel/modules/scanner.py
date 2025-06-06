import socket

def scan_ports(target):
    print(f"[+] Scanning {target}...")
    for port in range(1, 1025):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"[OPEN] Port {port}")
            s.close()
        except:
            pass