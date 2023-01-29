import subprocess
import os


def chroot(directory):
    print("Chrooting...")
    subprocess.run(["chroot", directory, "/bin/bash"])


def chroot_gui(directory, tty):
    print("Chrooting and starting gui...")
    subprocess.run(
        [
            "/bin/sh",
            os.path.dirname(os.path.realpath(__file__)) + "/shellscripts/rungui.sh",
            directory,
            tty,
            "2",
        ]
    )
