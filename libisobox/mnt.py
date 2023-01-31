import subprocess
import sys
import os


def tempmount_iso(path):
    print("Mounting iso to /tmp/isobox_mount")
    if not os.path.exists("/tmp/isobox_mount"):
        os.mkdir("/tmp/isobox_mount")
    subprocess.run(["mount", path, "/tmp/isobox_mount"])
