import requests
from colorama import Fore

def enumerate_subdomains(domain):
    print(f"  {Fore.YELLOW}-> Querying multiple OSINT databases for {domain}...")
    subdomains = set()
    
    # --- SOURCE 1: HackerTarget API (Extremely Fast & Reliable) ---
    try:
        ht_url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
        response = requests.get(ht_url, timeout=15)
        if response.status_code == 200 and "error" not in response.text.lower():
            lines = response.text.split('\n')
            for line in lines:
                if ',' in line:
                    sub = line.split(',')[0].strip()
                    subdomains.add(sub)
    except Exception as e:
        pass # Silently fail and try the next source

    # --- SOURCE 2: Certificate Transparency Logs (crt.sh) ---
    try:
        crt_url = f"https://crt.sh/?q=%25.{domain}&output=json"
        headers = {"User-Agent": "GhostMap-Recon-Tool/1.0"}
        response = requests.get(crt_url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                name = entry.get('name_value', '')
                if '\n' in name:
                    for n in name.split('\n'):
                        subdomains.add(n.strip())
                else:
                    subdomains.add(name.strip())
    except Exception:
        print(f"  {Fore.MAGENTA}[!] crt.sh is currently overloaded. Relying on HackerTarget fallback data.")

    # Filter out wildcard certificates and the base domain itself
    clean_subdomains = [sub for sub in subdomains if not sub.startswith('*') and sub != domain]
    
    # Sort for consistent output
    clean_subdomains.sort()
    
    print(f"  {Fore.GREEN}[+] Discovered {len(clean_subdomains)} unique subdomains.")
    
    # Return top 50 to prevent massive PDF reports
    return clean_subdomains[:50]
