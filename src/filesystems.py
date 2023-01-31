import subprocess
import os


def mount_filesystems(mountpoint):
    print("Mounting useful filesystems...")

    subprocess.run(
        [
            "/bin/sh",
            os.path.dirname(os.path.realpath(__file__)) + "/shellscripts/mounts.sh",
            mountpoint,
        ]
    )


def umount_filesystems(mountpoint):
    print("Unmounting filesystems...")
    subprocess.run(
        [
            "/bin/sh",
            os.path.dirname(os.path.realpath(__file__)) + "/shellscripts/umount.sh",
            mountpoint,
        ],
    )
