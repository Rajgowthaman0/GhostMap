import nmap
import sys
from colorama import Fore

def scan_ports(target):
    print(f"  {Fore.YELLOW}-> Initializing Nmap engine against {target}...")
    nm = nmap.PortScanner()
    
    try:
        # Using -F for fast scan (top 100 ports), -sV for service/version detection
        # -Pn skips host discovery, assuming the host is online
        nm.scan(target, arguments='-F -sV -Pn')
        
        results = []
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    state = nm[host][proto][port]['state']
                    name = nm[host][proto][port]['name']
                    product = nm[host][proto][port].get('product', '')
                    version = nm[host][proto][port].get('version', '')
                    
                    if state == 'open':
                        full_service = f"{product} {version}".strip()
                        if not full_service:
                            full_service = name
                        
                        results.append({
                            'port': port,
                            'state': state,
                            'service': name,
                            'version': full_service
                        })
                        print(f"  {Fore.GREEN}[+] Port {port}/tcp is OPEN - {full_service}")
                        
        if not results:
            print(f"  {Fore.RED}[-] No open ports discovered.")
            
        return results
        
    except Exception as e:
        print(f"  {Fore.RED}[!] Nmap could not be run. Is it installed? (Error: {str(e)[:50]}...)")
        return []
