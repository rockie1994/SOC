# Day 5: Hidden File Finder

## Project Overview

This is a Python-based SOC detection tool designed to identify stealthy files on a system. Attackers frequently hide malware, scripts, or stolen data by setting the file attribute to "Hidden" or "System" (MITRE ATT&CK T1564.001). This script scans a target directory and flags any files that possess these stealthy attributes.

## How It Works

1. Directory Reading: Uses `os.listdir()` to get a list of every file in the target folder.
2. Attribute Checking: Uses Python's `subprocess` module to run the Windows `attrib` command on each file.
3. The "Slice" Fix: Extracts only the first 10 characters of the command output (`attributes[:10]`). This prevents false positives from folder names (like `C:\Users\Harsh\...`) that might contain the letters "H" or "S".
4. Detection: Checks if the letter "H" (Hidden) or "S" (System) is present in the attribute flags and triggers a high-priority alert.

## Debugging Log (The Path False Positive)

Issue: Initially, the script flagged normal files as hidden. Because the script checked the entire output string for the letter "H", it was accidentally matching the letter "H" in the folder path (e.g., `C:\Users\Hacker\Desktop`).
Fix: I used Python string slicing to isolate only the first 10 characters of Windows' output, which contains the actual attribute flags, completely ignoring the file path.

## How to Run

1. Ensure you have Python installed on your system.
2. Clone this repository and navigate to the `SOC-day5` folder.
3. Create a folder named `test-folder` (or `test_folder`) in the same directory as the script.
4. Put some normal files and some hidden files (created via Windows Properties) inside the test folder.
5. Run the script: python hidden_finder.py


Sample Output

--- HIDDEN FILE SCANNER: test-folder ---

[OK] Normal file found: normal.txt
[ALERT] Hidden or System File Detected: secret.txt

Tech Stack:

Language: Python 3
Libraries: os, subprocess (built-in standard library)

Future Improvements:

Cross-Platform Support: The attrib command is Windows-only. Future versions should check if the file name starts with a dot (.) to support Linux and Mac.

Whitelisting: Ignore known safe hidden files like desktop.ini or Thumbs.db to reduce noise.

Hash Extraction: Automatically generate an MD5 hash of any hidden file found and send it to VirusTotal for analysis.

Live Integration: Use the winreg library to search the Windows Registry for unauthorized hidden files rather than just a local folder.