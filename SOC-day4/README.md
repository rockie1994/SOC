## Day 4: USB Device Tracker

## Project Overview

This is a Python-based SOC detection tool designed to identify unauthorized hardware additions (MITRE ATT&CK T1200). It parses system logs (simulating Windows Registry entries) to detect when a USB device is connected and specifically flags any device marked as "Unauthorized". Attackers and malicious insiders often use unauthorized USB drives to exfiltrate data or introduce malware.

## How It Works
1. Log Ingestion: Reads simulated USB connection logs (`usb_registry.txt`).
2. Filtering: Ignores non-USB events and only processes lines containing `USB Connected`.
3. Status Extraction: Uses Python's `list.index()` method to dynamically locate the keyword `Status:` and extract the value immediately following it.
4. Alerting: If the status is "Unauthorized", it extracts the device name and triggers a high-priority alert with the timestamp.

## Debugging Log
Issue: The script would crash if it encountered a USB device (like a standard mouse) that did not have a "Status:" field in the log.
Fix: I added an `if "Status:" in parts:` check before attempting to extract the status. This ensures the script only evaluates devices that actually have an authorization status, preventing errors.

## How to Run
1. Ensure you have Python installed on your system.
2. Clone this repository and navigate to the `SOC-day4` folder.
3. Ensure both `usb_tracker.py` and `usb_registry.txt` are in the same directory.
4. Run the script: python usb_tracker.py

Sample Output:

--- USB DEVICE TRACKER ---

[ALERT] Unauthorized USB Detected!
           Device: SanDisk | Time: 11:30:00
           Details: 2026-10-27 11:30:00 - USB Connected - Device: SanDisk Extreme 128GB - Serial: S888 - Status: Unauthorized

[ALERT] Unauthorized USB Detected!
           Device: Unknown | Time: 02:14:00
           Details: 2026-10-27 02:14:00 - USB Connected - Device: Unknown Storage Device - Serial: UNKNOWN123 - Status: Unauthorized

Tech Stack:

Language: Python 3
Libraries: None (uses built-in standard library)

Future Improvements:

Live Integration: Parse the actual Windows Registry path SYSTEM\CurrentControlSet\Enum\USBSTOR using Python's winreg library instead of a text file.

Hash Verification: Automatically calculate the serial number or hash of the USB drive to verify it against a known corporate whitelist.

Volume Alert: Flag if more than 50GB of data is copied to an unauthorized USB drive within a 10-minute window.