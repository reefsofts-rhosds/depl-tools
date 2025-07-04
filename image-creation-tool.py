# Depl-Tools v1.0
# Image Creation Tool

# Assuming the deployment share is mounted as /depl-share

import subprocess

subprocess.run("lsblk")
disk_id = input("Type in the disk/partition ID given above corresponding to the disk/partition that you want to image: ")
image_name = input("Type in the name of the image: ")
print("Starting disk imaging, please wait...")
subprocess.run(["sudo", "dd", "if=/dev/%s" % disk_id, "of=/depl-share/%s" % image_name])
