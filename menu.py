# Depl-Tools v1.0
# Global Menu
import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return False

# Unmount the share if it's already mounted
run_command(["sudo", "umount", "/depl-share"])

# Mount the remote share
if run_command(["sudo", "curlftpfs", "depl-share-access:depl-share-access@192.168.1.27:/", "/depl-share"]):
    #subprocess.run(["clear"])
    print("Depl-Tools")
    print("Global Menu")
    print("Available Actions")
    print("1. Create image of this computer")
    print("2. Apply an image onto this computer")
    print("3. Use Finnix Shell")

    chosen_action = input("Choose what action you want to perform: ")
    if chosen_action == "1":
        print("Launching Image Creation Tool")
        subprocess.run(["python3", "image-creation-tool.py"])
    elif chosen_action == "2":
        print("Launching Image Application Tool")
    elif chosen_action == "3":
        print("Launching Finnix Shell")
else:
    print("Failed to mount the remote share. Please check the error messages above.")
