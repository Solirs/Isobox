import subprocess
import os


def chroot(directory):
    subprocess.run(["chroot", directory])
