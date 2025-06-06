from modules.banner import show_banner
from modules.scanner import scan_ports
from modules.geoip import get_ip_info
from modules.network import get_local_info
from modules.phishing_detector import is_phishing

def main():
    show_banner()
    while True:
        print("\n[1] Port Scanner\n[2] GeoIP Lookup\n[3] Network Info\n[4] Phishing Detector\n[0] Exit")
        choice = input("Select an option: ")

        if choice == "1":
            target = input("Enter IP or domain: ")
            scan_ports(target)

        elif choice == "2":
            ip = input("Enter IP: ")
            data = get_ip_info(ip)
            for k, v in data.items():
                print(f"{k}: {v}")

        elif choice == "3":
            info = get_local_info()
            for k, v in info.items():
                print(f"{k}: {v}")

        elif choice == "4":
            url = input("Enter URL: ")
            if is_phishing(url):
                print("⚠️  Warning: URL looks suspicious!")
            else:
                print("✅ URL seems safe.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()