# The Event ID for a cleared audit log is 1102
SUSPICIOUS_EVENT_ID = "1102"

print("--- AUDIT LOG CLEARED DETECTION REPORT ---")

with open("audit.log", "r") as log_file:
    for line in log_file:
        
        # Split the line into words
        parts = line.split(" ")
        
        # Check if "ID:" is in the line to prevent errors
        if "ID:" in parts:
            
            # Instantly find the index of "ID:" and grab the next word
            event_id = parts[parts.index("ID:") + 1]
            
            # Check if the Event ID matches our suspicious ID
            if event_id == SUSPICIOUS_EVENT_ID:
                # Grab the user who cleared the log
                user = "Unknown"
                if "User:" in parts:
                    user = parts[parts.index("User:") + 1]
                    
                print(f"🚨 [CRITICAL ALERT] Audit Log Cleared!")
                print(f"           Cleared by User: {user}")
                print(f"           Details: {line.strip()}\n")