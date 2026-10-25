# Day 1: Failed Login Tracker (Brute Force Detection)

## Project Overview
This is a Python-based SOC (Security Operations Center) detection tool designed to analyze server authentication logs. It identifies Brute Force attacks by tracking the number of failed login attempts from individual IP addresses and triggering an alert when a specific threshold is breached.

## How It Works
1. Log Ingestion: The script reads a simulated authentication log file (`sample_log.txt`) line by line.
2. Filtering: It ignores successful logins and only focuses on lines containing `FAILED LOGIN`.
3. Data Extraction: Instead of relying on fixed word positions (which break if log formats change), the script dynamically searches for the keyword `IP:` and extracts the value immediately following it.
4. Tracking and Alerting: It uses a Python dictionary to maintain a tally of failures per IP. If an IP fails 3 or more times (the `ALERT_THRESHOLD`), the script prints a high-priority alert to the console.

## Debugging Log (The "Hyphen" Bug)
Issue: During initial testing, the script outputted `IP: -`. Because the log file used hyphens (`-`) separated by spaces, the script's initial blind positional parsing (`parts[5]`) grabbed a hyphen instead of the IP address.

Fix: I rewrote the parsing logic to use a `for` loop to iterate through the split string, locate the exact string `"IP:"`, and grab the index right after it (`parts[i + 1]`). This makes the tool robust and resistant to minor formatting changes.

## How to Run
1. Ensure you have Python installed on your system.
2. Clone this repository and navigate to the folder.
3. Ensure both `detector.py` and `sample_log.txt` are in the same directory.
4. Run the script:

```bash
python detector.py

SAMPLE OUTPUT

--- SOC DETECTION REPORT ---
[ALERT] Brute Force Detected! IP: 192.168.1.50 failed 6 times.
[OK] IP: 10.0.0.15 failed 1 times. (Below threshold)
[ALERT] Brute Force Detected! IP: 172.16.254.1 failed 5 times.
[OK] IP: 192.168.1.100 failed 1 times. (Below threshold)

Tech Stack

Language: Python 3
Libraries: None (uses built-in standard library)

Future Improvements

1. Real-Time Log Ingestion: Modify the script to tail a live log file (like /var/log/auth.log) in real-time using a library like watchdog, rather than parsing a static .txt file.

2. Automated Incident Response (SOAR): Integrate the script with a firewall API (like UFW or iptables) or a cloud security group (AWS) to automatically block the offending IP address once the threshold is breached.

3. SIEM Integration: Format the output into JSON or CEF (Common Event Format) so it can be easily ingested by enterprise SIEM tools like Splunk, Elastic, or Microsoft Sentinel.

4. Threat Intelligence Enrichment: Before alerting, the script could query an API (like AbuseIPDB or VirusTotal) to see if the attacking IP is a known malicious server or TOR exit node.

5. Alerting Channels: Replace the console print statements with webhooks to send instant notifications to a Discord channel, Slack workspace, or Microsoft Teams.

6. Geolocation Tracking: Use an IP geolocation library to determine the country of origin for the attacking IP and add it to the alert.

7. Time-Window Analysis: Instead of just a raw count, implement a sliding time window (e.g., "5 failed attempts within 60 seconds") to detect rapid automated scripts rather than slow, manual guessing.