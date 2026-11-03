# Define the Event IDs that we consider suspicious
# 4720: User account created
# 4732: User added to a local group (like Administrators)
SUSPICIOUS_EVENT_IDS = ["4720", "4732"]

print("--- LOCAL ADMIN CREATION DETECTION REPORT ---")

with open("auth_logs.txt", "r") as log_file:
    for line in log_file:
        
        # Split the line into words
        parts = line.split(" ")
        
        # Check if "ID:" is in the line to prevent errors
        if "ID:" in parts:
            
            # Instantly find the index of "ID:" and grab the next word
            event_id = parts[parts.index("ID:") + 1]
            
            # Check if the Event ID is in our suspicious list
            if event_id in SUSPICIOUS_EVENT_IDS:
                print(f"🚨 [ALERT] Privilege Escalation Detected! Event ID: {event_id}")
                print(f"           Details: {line.strip()}\n")