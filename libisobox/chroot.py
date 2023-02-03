import subprocess
import os


def chroot(directory, user):
    print("Chrooting...")
    home = "/home/" + user if user != "root" else "/root"
    subprocess.run(
        [
            "/bin/sh",
            os.path.dirname(os.path.realpath(__file__)) + "/shellscripts/chroot.sh",
            directory,
            user,
            home,
        ]
    )


def chroot_run(directory, user, program):
    home = "/home/" + user if user != "root" else "/root"
    subprocess.run(
        [
            "/bin/sh",
            os.path.dirname(os.path.realpath(__file__)) + "/shellscripts/chroot_run.sh",
            directory,
            user,
            home,
            program,
        ]
    )


def chroot_gui(directory, tty, display, user):
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
