# whois_module.py
import whois


def get_whois_info(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except Exception as e:
        return f"Error occurred while fetching WHOIS information: {e}"
