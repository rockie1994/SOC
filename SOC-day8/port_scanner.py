# We use a dictionary to track IPs. 
# The value for each IP will be a "Set" of ports.
ip_ports_scanned = {}

# If an IP touches this many unique ports, it's a scan.
PORT_THRESHOLD = 5

print("--- PORT SCAN DETECTION REPORT ---")

with open("network.log", "r") as log_file:
    for line in log_file:
        parts = line.split(" ")
        
        # Find the IP and the Port
        if "IP:" in parts and "Port:" in parts:
            source_ip = parts[parts.index("IP:") + 1]
            dest_port = parts[parts.index("Port:") + 1]
            
            # If this is a new IP, create an empty Set for it
            if source_ip not in ip_ports_scanned:
                ip_ports_scanned[source_ip] = set()
            
            # Add the port to the IP's Set (duplicates are ignored automatically)
            ip_ports_scanned[source_ip].add(dest_port)

# Now, check the results
for ip, ports in ip_ports_scanned.items():
    unique_port_count = len(ports) # Count how many unique ports are in the Set
    
    if unique_port_count >= PORT_THRESHOLD:
        print(f"🚨 [ALERT] Port Scan Detected! IP: {ip} touched {unique_port_count} unique ports.")
    else:
        print(f"✅ [OK] Normal traffic. IP: {ip} touched {unique_port_count} port(s).")