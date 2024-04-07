# urlscan_module.py
import requests
import time
import json


def submit_to_urlscan(url, api_key):
    headers = {'API-Key': api_key, 'Content-Type': 'application/json'}
    data = {"url": url, "visibility": "public"}
    response = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, json=data)
    if response.status_code == 200:
        scan_uuid = response.json().get('uuid')
        return scan_uuid
    else:
        print(f"[URLSCAN] RESPONSE={response.status_code}")
        return None


def get_urlscan_result(scan_uuid, api_key, retries=4, delay=15):
    result_url = f'https://urlscan.io/api/v1/result/{scan_uuid}/'
    headers = {'API-Key': api_key}

    for attempt in range(retries):
        time.sleep(delay)  # Wait before checking if the scan is ready
        response = requests.get(result_url, headers=headers)
        if response.status_code == 200:
            scan_data = response.json()
            return scan_data
        else:
            print(f"[URLSCAN] ATTEMPT={attempt + 1}/{retries}, REASON=FAILED_TO_FETCH_RESULTS, STATUS={response.status_code}")

    return None


def scan(url, api_key):
    scan_uuid = submit_to_urlscan(url, api_key)
    if scan_uuid:
        print("Scan submitted successfully.")
        print("Waiting for scan results...")
        scan_data = get_urlscan_result(scan_uuid, api_key)
        if scan_data:
            return scan_data
        else:
            return "Failed to retrieve scan results."
    else:
        return "Failed to submit the URL for scanning."
