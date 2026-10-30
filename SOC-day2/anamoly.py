# Define what hours are considered "off-hours" (12 AM to 5 AM)
# We use strings to match the exact format in the log.
SUSPICIOUS_HOURS = ["00", "01", "02", "03", "04", "05","06",
                    "07", "08", "09", "10", "11", "14"]

print("--- SUCCESSFUL LOGIN ANOMALY REPORT ---")

with open("auth_logs.txt", "r") as log_file:
    for line in log_file:
        # We only care about successful logins
        if "SUCCESS LOGIN" in line:
            
            # Split the line into words
            parts = line.split(" ")
            
            # The time is the second word (index 1), e.g., "09:15:00"
            time_string = parts[1]
            
            # We only want the hour part (the first two characters), e.g., "09"
            hour = time_string[0:2]
            
            # Extract the User and IP using our smart parsing logic
            user = "Unknown"
            ip = "Unknown"
            for i in range(len(parts)):
                if parts[i] == "User:":
                    user = parts[i + 1]
                if parts[i] == "IP:":
                    ip = parts[i + 1]
            
            # Check if the hour is in our suspicious list
            if hour in SUSPICIOUS_HOURS:
                print(f"🚨 [ALERT] Off-hours Login! User: {user} logged in at {time_string} from IP: {ip}")
            else:
                print(f"✅ [OK] Normal hours login. User: {user} at {time_string}")