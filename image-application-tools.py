# Depl-Tools v1.0
# Image Creation Tool

# Assuming the deployment share is mounted as /depl-share

import subprocess

subprocess.run("clear")
subprocess.run("ls", "/depl-share")
image_name = input("Type in the image name given above corresponding to the the image you want to apply: ")
subprocess.run("lsblk")
disk_id = input("Type in the disk ID corresponding to the disk you want to apply the image to: ")
print("Starting image application, please wait...")
subprocess.run(["sudo", "dd", "if=/dev/%s" % image_name, "of=/depl-share/%s" % disk_id])
