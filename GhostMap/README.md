# 👻 GhostMap: Advanced Attack Surface Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-Compatible-black?style=for-the-badge&logo=kali-linux)
![Security](https://img.shields.io/badge/Security-OSINT-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**GhostMap** is a powerful, Python-based automated reconnaissance framework designed for cybersecurity professionals, penetration testers, and ethical hackers. It streamlines the initial phases of a security assessment by automating deep domain intelligence gathering, subdomain enumeration, network scanning, and vulnerability mapping, culminating in a professional, client-ready PDF report.

Developed as a capstone project during a cybersecurity , GhostMap demonstrates proficiency in Python scripting, network protocols, OSINT gathering, and security tool automation (like Nmap).

---

## 🌟 Key Features

- **Deep Domain Intelligence:** Automatically resolves target IPs, identifies geolocation data, Hosting/ISP providers, and performs passive web server banner grabbing.
- **Automated Subdomain Enumeration:** Leverages multiple OSINT APIs (HackerTarget and crt.sh) to quickly discover subdomains without triggering alarms.
- **Intelligent Port Scanning:** Utilizes the `python-nmap` library to perform rapid service and version detection on discovered assets.
- **Professional PDF Reporting:** Automatically generates a comprehensive `ghostmap_report.pdf` using `fpdf`, detailing the attack surface of the target exactly how a consulting firm would present it.
- **Cross-Platform & Kali Ready:** Designed to work flawlessly on Kali Linux, Parrot OS, and standard Linux/Windows distributions.

---

## 🛠️ Installation & Setup

GhostMap requires Python 3.8+ and Nmap installed on your system. 

### 1. Install System Dependencies (Kali/Debian)
```bash
sudo apt-get update
sudo apt-get install nmap python3-pip python3-venv
```

### 2. Clone the Repository
```bash
git clone https://github.com/Rajgowthaman0/GhostMap.git
cd GhostMap
```

### 3. Create Virtual Environment & Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 Usage

Running GhostMap is straightforward. Provide the target domain using the `-t` flag. Ensure your virtual environment is active!

```bash
python ghostmap.py -t example.com
```

### Advanced Usage (Custom Output)
```bash
python ghostmap.py -t target.com -o /path/to/custom_report.pdf
```

---

## 🧠 Project Architecture

```text
GhostMap/
├── ghostmap.py             # Main execution script and CLI handler
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── modules/
    ├── __init__.py         # Package initializer
    ├── domain_info.py      # Extracts IP, Geolocation, and ISP data
    ├── subdomain_enum.py   # OSINT-based subdomain discovery
    ├── port_scanner.py     # Nmap automation and parsing
    └── report_generator.py # FPDF automated report construction
```

---

## 💼 Why this project? (For Hiring Managers & Recruiters)

This project was built to demonstrate:
1. **Automation of Security Workflows:** Reducing manual effort in the recon phase.
2. **Python for Cybersecurity:** Utilizing APIs, handling networks (sockets/Nmap), and processing JSON data.
3. **Report Writing:** Automatically generating executive summaries, a critical skill for penetration testers.
4. **Tool Integration:** Bridging the gap between raw tool output (Nmap XML/CLI) and structured, actionable intelligence.

---

## ⚠️ Disclaimer

**GhostMap is strictly for educational purposes and ethical hacking.** 
Do not use this tool against any networks or systems for which you do not have explicit, written permission to test. The author is not responsible for any misuse or damage caused by this program.
