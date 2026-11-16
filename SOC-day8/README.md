# Day 8: Port Scan Detector

## Project Overview

This is a Python-based SOC detection tool designed to identify network reconnaissance (MITRE ATT&CK T1046). Before launching an attack, hackers use tools like Nmap to rapidly scan a server for open ports. This script parses firewall traffic logs and triggers an alert if a single IP address touches too many unique destination ports within the log file.

## How It Works

1. Log Ingestion: Reads simulated network logs (`network.log`).
2. Data Extraction: Dynamically searches for `IP:` and `Port:` tags to extract the source IP and destination port.
3. The Power of Sets: It uses a Python Dictionary where the values are **Sets**. A Set automatically removes duplicates. If a normal user refreshes a webpage 50 times on port 443, the Set still only counts it as 1 unique port.
4. Threshold Alerting: If an IP touches 5 or more unique ports, it flags a Port Scan.

## Debugging Log

Issue: Initially, I used a simple counter (`count += 1`) to track port connections. However, this caused false positives because normal users can connect to the same port (like 443) dozens of times a minute.

Fix: I switched the tracking variable to a `set()`. This allowed the script to only count *unique* ports, completely eliminating the false positives from repeated connections to the same service.

## How to Run

1. Ensure Python is installed.
2. Run the script: python port_scanner.py

Sample Output>:

--- PORT SCAN DETECTION REPORT ---
[ALERT] Port Scan Detected! IP: 192.168.1.50 touched 6 unique ports.
[OK] Normal traffic. IP: 10.0.0.15 touched 1 port(s).
[OK] Normal traffic. IP: 172.16.254.1 touched 1 port(s).

Tech Stack:

Language: Python 3
Libraries: None (uses built-in standard library)

Future Improvements:

1. Time-Window Analysis: Add a time constraint. Scanning 5 ports in 1 second is an attack; scanning 5 ports over 5 hours is normal behavior.

2. SIEM Integration: Export the alerts to JSON for Splunk or Elastic ingestion.

3. Geo-IP Enrichment: Query an API to find out which country the scanning IP belongs to.