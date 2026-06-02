import argparse
import sys
from colorama import init, Fore, Style
from modules.domain_info import get_domain_intelligence
from modules.port_scanner import scan_ports
from modules.subdomain_enum import enumerate_subdomains
from modules.report_generator import generate_pdf_report

init(autoreset=True)

def print_banner():
    # A unique, badass name and title
    banner = r"""
{Fore.CYAN}{Style.BRIGHT}
   ____ _               _   __  __             
  / ___| |__   ___  ___| |_|  \/  | __ _ _ __  
 | |  _| '_ \ / _ \/ __| __| |\/| |/ _` | '_ \ 
 | |_| | | | | (_) \__ \ |_| |  | | (_| | |_) |
  \____|_| |_|\___/|___/\__|_|  |_|\__,_| .__/ 
                                        |_|    
{Fore.YELLOW}GhostMap - Advanced Attack Surface Analyzer
{Fore.WHITE}Automated Threat Intelligence & OSINT Collector
    """
    print(banner.format(Fore=Fore, Style=Style))

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="GhostMap - Recon Framework")
    parser.add_argument("-t", "--target", required=True, help="Target domain (e.g., example.com)")
    parser.add_argument("-o", "--output", default="ghostmap_report.pdf", help="Output PDF report filename")
    
    args = parser.parse_args()
    target = args.target
    output_file = args.output

    print(f"{Fore.GREEN}[+] Starting intelligence gathering on: {Style.BRIGHT}{target}")

    # Step 1: Deep Domain Intelligence
    print(f"\n{Fore.BLUE}[*] Phase 1: Gathering Deep Domain Intelligence...")
    domain_intel = get_domain_intelligence(target)

    # Step 2: Subdomain Enumeration
    print(f"\n{Fore.BLUE}[*] Phase 2: Enumerating Subdomains via OSINT...")
    subdomains = enumerate_subdomains(target)
    
    # Step 3: Port Scanning
    print(f"\n{Fore.BLUE}[*] Phase 3: Active Network Scanning...")
    scan_results = scan_ports(target)

    # Step 4: Reporting
    print(f"\n{Fore.BLUE}[*] Phase 4: Compiling Intelligence Report...")
    generate_pdf_report(target, domain_intel, subdomains, scan_results, output_file)

    print(f"\n{Fore.GREEN}[+] Operations complete! Report securely saved as {Style.BRIGHT}{output_file}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Scan interrupted by user. Exiting...")
        sys.exit(1)
