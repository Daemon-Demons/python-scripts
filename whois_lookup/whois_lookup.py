import whois
import csv
import os
from datetime import datetime
from pathlib import Path

# Path to the directory where reports will be saved
REPORT_DIR = Path('./whois_lookup/reports/')
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# Define CSV file path
CSV_FILE = REPORT_DIR / 'whois_report.csv'

# Define the fields for the CSV
FIELDS = ['Domain', 'Registrar', 'Creation Date', 'Expiry Date', 'Nameservers', 'Updated Date', 'Registrant Organization', 'Registrant Country']

def safe_field(val):
    if isinstance(val, list):
        val = val[0] if val else 'N/A'
    if isinstance(val, datetime):
        return val.strftime('%Y-%m-%d')
    return str(val) if val else 'N/A'

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        data = {
            'Domain': domain,
            'Registrar': safe_field(w.registrar),
            'Creation Date': safe_field(w.creation_date),
            'Expiry Date': safe_field(w.expiration_date),
            'Nameservers': ', '.join(w.nameservers) if isinstance(w.nameservers, list) else (w.nameservers or 'N/A'),
            'Updated Date': safe_field(w.updated_date),
            'Registrant Organization': safe_field(getattr(w, 'org', None)),
            'Registrant Country': safe_field(getattr(w, 'country', None)),
        }
        return data
    except Exception as e:
        print(f"Error looking up {domain}: {e}")
        return None

def append_to_csv(data):
    file_exists = CSV_FILE.exists()
    write_header = not file_exists or CSV_FILE.stat().st_size == 0

    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        if write_header:
            writer.writeheader()
        writer.writerow(data)

def main():
    domains_input = input("Enter domains separated by commas: ")
    domains = [d.strip() for d in domains_input.split(',') if d.strip()]
    if not domains:
        print("No domains entered.")
        return

    for domain in domains:
        data = whois_lookup(domain)
        if data:
            append_to_csv(data)
            print(f"Appended data for {domain}")
        else:
            print(f"Failed to retrieve data for {domain}")

if __name__ == '__main__':
    main()