# We create a dictionary to keep track of how many times an IP fails.
failed_attempts = {}

# This is our "Threshold". If an IP fails 3 times, we alert.
ALERT_THRESHOLD = 3

# Open the log file and read it line by line
with open("sample_log.txt", "r") as log_file:
    for line in log_file:
        # Check if the word "FAILED LOGIN" is in the current line
        if "FAILED LOGIN" in line:
            
            # Split the line by spaces
            parts = line.split(" ")
            
            
            # Loop through the words to find the exact word "IP:"
            for i in range(len(parts)):
                if parts[i] == "IP:":
                    # The IP address is the very next word after "IP:"
                    ip_address = parts[i + 1]
                    break
            
            # Count the failures for this specific IP
            if ip_address in failed_attempts:
                failed_attempts[ip_address] += 1
            else:
                failed_attempts[ip_address] = 1

# Once the file is read, check which IPs crossed the threshold
print("--- SOC DETECTION REPORT ---")
for ip, count in failed_attempts.items():
    if count >= ALERT_THRESHOLD:
        print(f"[ALERT] Brute Force Detected! IP: {ip} failed {count} times.")
    else:
        print(f"[OK] IP: {ip} failed {count} times. (Below threshold)")