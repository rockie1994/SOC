# Day 6: Audit Log Cleared Detector

## Project Overview

This is a Python-based SOC detection tool designed to catch Defense Evasion (MITRE ATT&CK T1070.001). When attackers compromise a system, they often clear the Windows Event Logs to erase evidence of their activity. This script parses Windows Security Logs and triggers a critical alert if it detects Event ID 1102 (The audit log was cleared).

## How It Works

1. Log Ingestion: Reads simulated Windows Event Logs (`windows_audit.log`).
2. Data Extraction: Dynamically searches for the keyword `ID:` to extract the Event ID using `list.index()`.
3. Alerting: Compares the extracted Event ID against the known "log cleared" ID (1102). If it matches, it attempts to extract the username responsible and triggers a high-priority alert.

## Debugging Log

Issue: I wanted the alert to show *who* cleared the log, but I realized not every log line has a "User:" field. If the script tried to grab the user from a line without one, it would crash.

Fix: I added an `if "User:" in parts:` check. If the field exists, it grabs the name; if not, it defaults to "Unknown" so the script continues running without errors.

## How to Run

1. Ensure Python is installed.
2. Navigate to the `SOC-day6` folder.
3. Ensure both `log_clearer.py` and `windows_audit.log` are in the same directory.
4. Run the script: python log_clearer.py

Sample Output:

--- AUDIT LOG CLEARED DETECTION REPORT ---
[CRITICAL ALERT] Audit Log Cleared!
           Cleared by User: hacker_admin
           Details: 2026-10-29 11:35:00 - Event ID: 1102 - The audit log was cleared - User: hacker_admin

Tech Stack:

Language: Python 3
Libraries: None (uses built-in standard library)

Future Improvements:

1. Live Integration: Use the pywin32 library to monitor the live Windows Security log in real-time rather than reading a static text file.

2. Correlation: Trigger an even higher severity alert if an account is created (Event ID 4720) and the logs are cleared (Event ID 1102) within a 5-minute window.

3. Centralized Logging: Send the alert to a remote Syslog server or SIEM immediately, because if the attacker clears the local logs, they might also clear the evidence of this alert.