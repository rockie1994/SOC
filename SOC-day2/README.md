# Day 2: Successful Login Anomaly

## Project Overview
This is a Python-based SOC detection tool designed to identify suspicious account activity. It parses authentication logs and flags any successful login that occurs during "off-hours" (e.g., between 12:00 AM and 5:00 AM), which is a common tactic for attackers trying to evade detection.

## How It Works
1. Log Ingestion: Reads simulated logs (`auth_logs.txt`).
2. Filtering: Ignores failed logins and only looks at `SUCCESS LOGIN` events.
3. Time Extraction: Splits the timestamp string to isolate the hour (e.g., `03` from `03:14:00`).
4. Threshold Alerting: Checks if the hour exists in the `SUSPICIOUS_HOURS` list and triggers an alert.

## How to Run
1. Ensure Python is installed.
2. Run the script: python anomaly.py

## Sample Output

--- SUCCESSFUL LOGIN ANOMALY REPORT ---
[OK] Normal hours login. User: john.doe at 09:15:00
[OK] Normal hours login. User: sarah.smith at 14:30:22
[OK] Normal hours login. User: admin at 17:45:10
[OK] Normal hours login. User: mike.jones at 23:55:00
[ALERT] Off-hours Login! User: admin logged in at 03:14:00 from IP: 185.15.20.10
[OK] Normal hours login. User: sarah.smith at 08:30:00

## Tech Stack:

Language: Python 3
Libraries: None (uses built-in standard library)

## Future Improvements:

1. Dynamic Baseline: Instead of a hardcoded list, the script could learn what "normal" hours are for each specific user and alert if they deviate from their own pattern.

2. Geolocation Tracking: Integrate an API to flag logins from unexpected countries.

3. Weekend Detection: Add logic to flag logins that happen on Saturdays and Sundays for corporate accounts.