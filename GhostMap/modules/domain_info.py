import socket
import requests
from colorama import Fore

def get_domain_intelligence(domain):
    print(f"  {Fore.YELLOW}-> Gathering deep intelligence for {domain}...")
    info = {
        'ip': 'Unknown',
        'location': 'Unknown',
        'isp': 'Unknown',
        'server': 'Unknown'
    }
    
    # 1. Resolve IP Address
    try:
        ip = socket.gethostbyname(domain)
        info['ip'] = ip
        print(f"  {Fore.GREEN}[+] Resolved IP: {ip}")
    except socket.gaierror:
        print(f"  {Fore.RED}[!] Could not resolve IP for {domain}")
        return info

    # 2. Get Geolocation and ISP info via IP-API (Free OSINT API)
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                info['location'] = f"{data.get('city', '')}, {data.get('country', '')}"
                info['isp'] = data.get('isp', '')
                print(f"  {Fore.GREEN}[+] Location: {info['location']}")
                print(f"  {Fore.GREEN}[+] ISP/Hosting: {info['isp']}")
    except Exception as e:
        print(f"  {Fore.RED}[!] Could not fetch geolocation: {e}")

    # 3. Get Web Server Headers (Passive Banner Grabbing)
    try:
        url = f"http://{domain}"
        response = requests.get(url, timeout=10)
        server = response.headers.get('Server', 'Hidden/Unknown')
        info['server'] = server
        print(f"  {Fore.GREEN}[+] Web Server: {server}")
    except Exception:
        pass

    return info
