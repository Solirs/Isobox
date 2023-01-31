import subprocess
import os
import shutil


def unsquash(mountpoint, squashedpath):
    print("Unsquashing iso's squashfs...")
    if not os.path.exists(mountpoint):
        os.mkdir(mountpoint)
    os.chdir(mountpoint)
    shutil.copy2(squashedpath, mountpoint)
    subprocess.run(["unsquashfs", mountpoint + "/" + os.path.basename(squashedpath)])
    for direc in os.listdir(mountpoint + "/" + "squashfs-root"):
        shutil.move(mountpoint + "/" + "squashfs-root/" + direc, mountpoint)
    shutil.rmtree(mountpoint + "/" + "squashfs-root")
    os.remove(mountpoint + "/" + os.path.basename(squashedpath))
