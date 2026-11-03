# Day 3: New Local Admin Creation Tracker

## Project Overview
This is a Python-based SOC detection tool designed to detect Privilege Escalation. It parses Windows Security Event Logs and triggers an alert if a new user account is created (Event ID 4720) or if a user is added to a security-enabled local group (Event ID 4732). Attackers frequently perform these actions to establish persistence and maintain administrative access to a compromised system.

## How It Works
1. Log Ingestion: Reads simulated Windows Event Logs (`windows_security.log`).
2. Data Extraction: Splits each log line into words and dynamically locates the keyword `ID:` to extract the specific Windows Event ID.
3. Threshold Alerting: Compares the extracted Event ID against a predefined list of `SUSPICIOUS_EVENT_IDS` (4720 and 4732). If a match is found, it prints a high-priority alert with the full log details.

## Debugging Log
Issue: Initially, I used a `for` loop to iterate through every word in the log line to find the Event ID.
Fix: I refactored the code to use Python's built-in `list.index()` method. This instantly finds the position of `"ID:"` and grabs the next word (`+ 1`), making the code significantly shorter and more efficient.

## How to Run
1. Ensure you have Python installed on your system.
2. Ensure both `admin_tracker.py` and `auth_log.txt` are in the same directory.
3. Run the script: python admin_tracker.py

Sample Output:

--- LOCAL ADMIN CREATION DETECTION REPORT ---
[ALERT] Privilege Escalation Detected! Event ID: 4720
           Details: 2026-10-26 11:30:00 - Event ID: 4720 - A user account was created - New User: hacker_backdoor

[ALERT] Privilege Escalation Detected! Event ID: 4732
           Details: 2026-10-26 11:31:00 - Event ID: 4732 - A member was added to a security-enabled local group - Group: Administrators - Target User: hacker_backdoor

Tech Stack: 

Language: Python 3
Libraries: None (uses built-in standard library)

Future Improvements:

Whitelisting: If IT admins regularly create accounts, the script should whitelist specific admin usernames or IP addresses to reduce false positives.

Enrichment: Query an API to see if the newly created username exists in known threat databases.

Correlation: Alert if an account is created (4720) AND immediately added to the admin group (4732) within a 5-minute window.

Live Integration: Replace the text file with a live Windows Event Log API query using the pywin32 library.