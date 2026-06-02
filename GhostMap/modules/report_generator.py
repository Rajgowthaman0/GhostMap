from fpdf import FPDF
from datetime import datetime
import os

class ProfessionalPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font('Arial', 'B', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, 'GhostMap | Advanced Attack Surface Analyzer', 0, 1, 'R')
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f'CONFIDENTIAL - Page {self.page_no()}', 0, 0, 'C')

def generate_pdf_report(target, domain_intel, subdomains, scan_results, output_filename):
    pdf = ProfessionalPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # ----------------------------------------
    # PAGE 1: TITLE PAGE & EXECUTIVE SUMMARY
    # ----------------------------------------
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(41, 128, 185) 
    pdf.cell(0, 20, 'GhostMap Intelligence Report', 0, 1, 'C')
    
    pdf.set_font('Arial', 'I', 14)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 10, 'Automated Threat Intelligence & OSINT Collector', 0, 1, 'C')
    pdf.ln(15)
    
    # Target Scope block
    pdf.set_fill_color(240, 240, 240)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 10, ' Target Scope:', 1, 0, 'L', fill=True)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f' {target}', 1, 1, 'L')
    
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 10, ' Scan Date:', 1, 0, 'L', fill=True)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f' {datetime.now().strftime("%B %d, %Y - %H:%M:%S")}', 1, 1, 'L')
    pdf.ln(15)
    
    # Domain Intelligence Section
    pdf.set_font('Arial', 'B', 14)
    pdf.set_text_color(41, 128, 185)
    pdf.cell(0, 10, '1. Target Domain Intelligence', 0, 1, 'L')
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Arial', '', 11)
    
    pdf.cell(40, 8, ' IP Address:', 0, 0, 'L')
    pdf.cell(0, 8, domain_intel.get('ip', 'Unknown'), 0, 1, 'L')
    
    pdf.cell(40, 8, ' Geolocation:', 0, 0, 'L')
    pdf.cell(0, 8, domain_intel.get('location', 'Unknown'), 0, 1, 'L')
    
    pdf.cell(40, 8, ' ISP / Hosting:', 0, 0, 'L')
    pdf.cell(0, 8, domain_intel.get('isp', 'Unknown'), 0, 1, 'L')
    
    pdf.cell(40, 8, ' Web Server:', 0, 0, 'L')
    pdf.cell(0, 8, domain_intel.get('server', 'Unknown'), 0, 1, 'L')
    pdf.ln(10)

    # ----------------------------------------
    # PAGE 2: OSINT SUBDOMAIN ENUMERATION
    # ----------------------------------------
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(41, 128, 185)
    pdf.cell(0, 10, '2. OSINT Subdomain Enumeration', 0, 1, 'L')
    pdf.ln(5)
    
    pdf.set_font('Arial', 'B', 11)
    pdf.set_fill_color(41, 128, 185)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 8, f' Discovered Subdomains ({len(subdomains)} extracted)', 0, 1, 'L', fill=True)
    
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Arial', '', 10)
    
    if subdomains:
        for i, sub in enumerate(subdomains, 1):
            if i % 2 == 0:
                pdf.set_fill_color(245, 245, 245)
            else:
                pdf.set_fill_color(255, 255, 255)
            pdf.cell(0, 6, f"  {i}. {sub}", 0, 1, 'L', fill=True)
    else:
        pdf.cell(0, 6, "No subdomains discovered.", 0, 1)
        
    pdf.ln(10)
    
    # ----------------------------------------
    # PAGE 3: ACTIVE SCANNING
    # ----------------------------------------
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(41, 128, 185)
    pdf.cell(0, 10, '3. Active Port & Service Scanning', 0, 1, 'L')
    pdf.ln(5)
    
    if scan_results:
        pdf.set_font('Arial', 'B', 10)
        pdf.set_fill_color(41, 128, 185)
        pdf.set_text_color(255, 255, 255)
        
        col1, col2, col3, col4 = 20, 25, 40, 105
        
        pdf.cell(col1, 8, 'Port', 1, 0, 'C', fill=True)
        pdf.cell(col2, 8, 'State', 1, 0, 'C', fill=True)
        pdf.cell(col3, 8, 'Service', 1, 0, 'C', fill=True)
        pdf.cell(col4, 8, 'Version Detection', 1, 1, 'C', fill=True)
        
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('Arial', '', 10)
        
        for res in scan_results:
            version_str = res['version']
            if len(version_str) > 55:
                version_str = version_str[:52] + "..."
                
            pdf.cell(col1, 8, str(res['port']), 1, 0, 'C')
            pdf.cell(col2, 8, res['state'], 1, 0, 'C')
            pdf.cell(col3, 8, res['service'], 1, 0, 'C')
            pdf.cell(col4, 8, version_str, 1, 1, 'L')
    else:
        pdf.set_font('Arial', '', 10)
        pdf.cell(0, 8, "No open ports found or host appears to be down.", 1, 1, 'C')

    output_dir = os.path.dirname(output_filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    pdf.output(output_filename)
