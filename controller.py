# control_module.py
import virustotal_module
import urlscan_module
import output_module
import os
import json
import twitter_module


def get_api_key(config_file):
    with open(os.path.join("configs", config_file), "r") as f:
        config = json.load(f)
    return config["api_key"]


def main():
    url = input("Enter the URL to scan: ")
    print(f"Scanning URL: {url}")

    # Get API keys from config files
    vt_api_key = get_api_key("virustotal_config.json")
    urlscan_api_key = get_api_key("urlscan_config.json")

    # Run scans
    print("Running VirusTotal scan...")
    vt_result = virustotal_module.scan(url, vt_api_key)
    print("VirusTotal scan completed.")

    print("Running URLScan.io scan...")
    urlscan_result = urlscan_module.scan(url, urlscan_api_key)
    print("URLScan.io scan completed.")

    # Combine results
    results = {
        "VirusTotal": vt_result,
        "URLScan.io": urlscan_result
    }

    # Save results to file
    print("Saving results to file...")
    output_module.save_results(results)
    print("Results saved successfully.")

    # Start the twitter_module
    twitter_module.start_twitter_module()

    # Ask if the user wants to scan another URL
    another_scan = input("Do you want to scan another URL? (y/n) ")
    if another_scan.lower() == "y":
        main()
    else:
        print("Exiting the script...")


if __name__ == "__main__":
    main()
