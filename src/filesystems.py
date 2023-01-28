import subprocess
import os


def mount_filesystems():
    subprocess.run(
        [
            "/bin/sh",
            os.path.dirname(os.path.realpath(__file__)) + "/shellscripts/mounts.sh",
            "/mnt/debian",
        ]
    )


def umount_filesystems():
    subprocess.run(
        [
            "/bin/sh",
            os.path.dirname(os.path.realpath(__file__)) + "/shellscripts/umount.sh",
            "/mnt/debian",
        ]
    )
