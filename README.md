<div align="center">

# URL Analysis Tool

This repository contains a Python-based tool for analyzing URLs and detecting potential threats using various cybersecurity services like VirusTotal and URLScan.io. The tool combines the scan results with WHOIS information and provides a user-friendly interface to tweet the analysis findings or custom messages.

</div>

## Features

- Scan URLs using VirusTotal and URLScan.io APIs
- Retrieve WHOIS information for the analyzed domains
- Save the combined analysis results to numbered output files
- Interact with the Twitter API to post tweets containing the analysis results or custom text
- User-friendly command-line interface

<div align="center">

## ☕ [Support my work on Ko-Fi](https://ko-fi.com/thatsinewave)

</div>

## Repository Structure

- `controller.py`: The main entry point of the application, handling user input, coordinating the execution of various modules, and providing the user interface.
- `output_module.py`: Handles the formatting and saving of analysis results to output files in the `outputs` directory.
- `twitter_module.py`: Allows users to interact with the Twitter API to post tweets containing analysis results or custom text.
- `urlscan_module.py`: Interacts with the URLScan.io API to submit URLs for scanning and retrieve the scan results.
- `virustotal_module.py`: Interacts with the VirusTotal API to scan URLs and retrieve the analysis results.
- `whois_module.py`: Fetches WHOIS information for a given domain.
- `configs/`: Directory containing configuration files with API keys for VirusTotal, URLScan.io, and Twitter.
- `outputs/`: Directory where the analysis results are saved as numbered text files.

<div align="center">

# [Join my discord server](https://discord.gg/2nHHHBWNDw)

</div>

## Usage

1. Clone the repository or download the source code.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Obtain API keys for VirusTotal, URLScan.io, and Twitter, and create configuration files in the `configs` directory with the respective API keys.
4. Run the `controller.py` script.
5. Follow the prompts to enter a URL for scanning, tweet the results, or scan another URL.

## Configuration Files

The tool requires API keys for VirusTotal, URLScan.io, and Twitter. These keys should be stored in separate JSON files in the `configs` directory with the following structure:

- `virustotal_config.json`:
  ```json
  {
    "api_key": "your_virustotal_api_key"
  }
  ```

- `urlscan_config.json`:
  ```json
  {
    "api_key": "your_urlscan_api_key"
  }
  ```

- `twitter_config.json`:
  ```json
  {
    "consumer_key": "your_twitter_consumer_key",
    "consumer_secret": "your_twitter_consumer_secret",
    "access_token": "your_twitter_access_token",
    "access_token_secret": "your_twitter_access_token_secret"
  }
  ```

## Output Files

The analysis results are saved as numbered text files in the `outputs` directory. Each file contains the following information:

- Scanned URL
- Domain
- Registrar
- Creation and expiration dates
- Threat types
- IP addresses and countries associated with the URL
- Scan date
- Screenshot URL
- VirusTotal and URLScan.io report URLs

## Dependencies

This project requires the following Python libraries:

- `requests`
- `tweepy`
- `python-whois`

Install these dependencies by running `pip install -r requirements.txt` before running the application.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Follow the standard GitHub workflow for contributions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
