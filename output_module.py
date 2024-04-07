# output_module.py
import os
import json
from urllib.parse import urlparse
import whois_module


def format_url(url):
    parts = url.split(".")
    formatted_url = "[.]".join(parts)
    return formatted_url


def get_threat_types(vt_result):
    threat_types = set()
    scans = vt_result.get("scans", {})
    for scanner, result in scans.items():
        result_str = result.get("result", "").lower()
        if "phishing site" in result_str:
            threat_types.add("Phishing")
        elif "malicious site" in result_str:
            threat_types.add("Malicious")
        elif "malware" in result_str:
            threat_types.add("Malware")
        elif "suspicious" in result_str:
            threat_types.add("Suspicious")
    return ", ".join(sorted(threat_types))


def save_results(results):
    # Get the number of existing output files
    output_files = [f for f in os.listdir("outputs") if f.startswith("output")]
    output_number = len(output_files) + 1

    # Create the output file name
    output_filename = f"output{output_number}.txt"
    output_path = os.path.join("outputs", output_filename)

    # Write the results to the output file
    with open(output_path, "w") as f:
        vt_result = results["VirusTotal"]
        urlscan_result = results["URLScan.io"]

        # Get the data from VirusTotal and URLScan.io
        scanned_url = vt_result.get("url")
        scan_date = vt_result.get("scan_date")
        vt_permalink = vt_result.get("permalink")
        urlscan_reporturl = urlscan_result.get("task", {}).get("reportURL")
        ips = urlscan_result.get("lists", {}).get("ips", [])
        countries = urlscan_result.get("lists", {}).get("countries", [])
        screenshot_url = urlscan_result.get("task", {}).get("screenshotURL")

        # Get the domain from the scanned URL
        parsed_url = urlparse(scanned_url)
        domain = parsed_url.netloc

        # Get the threat types from VirusTotal results
        threat_types = get_threat_types(vt_result)

        # Get WHOIS information
        whois_info = whois_module.get_whois_info(domain)
        if isinstance(whois_info, dict):
            registrar = whois_info.get("registrar", "N/A")
            creation_date = whois_info.get("creation_date", "N/A")
            expiration_date = whois_info.get("expiration_date", "N/A")
        else:
            registrar = "N/A"
            creation_date = "N/A"
            expiration_date = "N/A"

        # Format the output
        f.write(f"NEW URL DISCOVERED ON {scan_date}\n")
        f.write(f"URL: {format_url(scanned_url)}\n")
        f.write(f"Domain: {format_url(domain)}\n")
        f.write(f"Registrar: {registrar}\n")
        f.write(f"Created at: {creation_date}\n")
        f.write(f"Expires at: {expiration_date}\n")
        f.write(f"Type: {threat_types}\n")
        f.write("IPs: " + ", ".join(ips) + "\n")
        f.write("Countries: " + ", ".join(countries) + "\n")
        f.write(f"Scanned at: {scan_date}\n")
        f.write(f"Screenshot: {screenshot_url}\n")
        f.write(f"VirusTotal Report: {vt_permalink}\n")
        f.write(f"URLScan report: {urlscan_reporturl}\n")
