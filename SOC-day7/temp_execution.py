print("--- TEMP FOLDER EXECUTION DETECTION REPORT ---")

with open("process_creation.log", "r") as log_file:
    for line in log_file:
        
        # Split the line into words
        parts = line.split(" ")
        
        # Look for the "Path:" tag to find where the program is running from
        if "Path:" in parts:
            file_path = parts[parts.index("Path:") + 1]
            
            # Check if the path contains "\Temp\" (case-insensitive)
            # We use .lower() to catch "temp", "Temp", and "TEMP"
            if "\\temp\\" in file_path.lower():
                
                # Extract the user who ran it
                user = "Unknown"
                if "User:" in parts:
                    user = parts[parts.index("User:") + 1]
                    
                print(f"🚨 [ALERT] Executable Running from Temp Folder!")
                print(f"           User: {user}")
                print(f"           File Path: {file_path}\n")