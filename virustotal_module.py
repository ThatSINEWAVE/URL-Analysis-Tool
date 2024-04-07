# virustotal_module.py
import requests


def scan(url, api_key):
    # VirusTotal API URL
    vt_url = "https://www.virustotal.com/vtapi/v2/url/report"

    # API parameters
    params = {
        "apikey": api_key,
        "resource": url
    }

    try:
        # Send the API request
        response = requests.get(vt_url, params=params)
        response.raise_for_status()

        # Get the scan results
        results = response.json()

        if results["response_code"] == 1:
            # Scan report available
            return results
        elif results["response_code"] == 0:
            # No scan report available
            return "No scan report available for the given URL."
        else:
            # Unknown response code
            return f"Unknown response code: {results['response_code']}"

    except requests.exceptions.RequestException as e:
        # Handle exceptions
        return f"Error occurred: {e}"
