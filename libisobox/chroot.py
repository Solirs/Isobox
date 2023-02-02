import subprocess
import os


def chroot(directory):
    print("Chrooting...")
    subprocess.run(
        [
            "/bin/sh",
            os.path.dirname(os.path.realpath(__file__)) + "/shellscripts/chroot.sh",
            directory,
        ]
    )


def chroot_gui(directory, tty, display):
    print("Chrooting and starting gui...")
    subprocess.run(
        [
            "/bin/sh",
            os.path.dirname(os.path.realpath(__file__)) + "/shellscripts/rungui.sh",
            directory,
            tty,
            display,
        ]
    )
