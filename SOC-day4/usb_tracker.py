print("--- USB DEVICE TRACKER ---")

with open("usb_registry.txt", "r") as log_file:
    for line in log_file:
        
        # Only look at lines where a USB was connected
        if "USB Connected" in line:
            parts = line.split(" ")
            
            # Check if the word "Status:" exists in this line
            if "Status:" in parts:
                
                # Grab the word right after "Status:"
                status = parts[parts.index("Status:") + 1]
                
                # If the status is Unauthorized, trigger an alert
                if status == "Unauthorized":
                    # Grab the device name for the alert
                    device_name = parts[parts.index("Device:") + 1] 
                    
                    print(f"🚨 [ALERT] Unauthorized USB Detected!")
                    print(f"           Device: {device_name} | Time: {parts[1]}")
                    print(f"           Details: {line.strip()}\n")