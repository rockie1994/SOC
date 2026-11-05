import os
import subprocess

TARGET_FOLDER = "test-folder"

print(f"--- HIDDEN FILE SCANNER: {TARGET_FOLDER} ---")

if os.path.exists(TARGET_FOLDER):
    for file_name in os.listdir(TARGET_FOLDER):
        file_path = os.path.join(TARGET_FOLDER, file_name)
        
        # Ask Windows for the file's attributes
        result = subprocess.run(["attrib", file_path], capture_output=True, text=True)
        attributes = result.stdout
        
        # THE FIX: Only look at the first 10 characters of the output. 
        # The attributes (like 'A', 'H', 'S') are always at the very beginning.
        attribute_flags = attributes[:10]
        
        if "H" in attribute_flags or "S" in attribute_flags:
            print(f"🚨 [ALERT] Hidden or System File Detected: {file_name}")
        else:
            print(f"✅ [OK] Normal file found: {file_name}")
else:
    print(f"Error: The folder '{TARGET_FOLDER}' does not exist.")