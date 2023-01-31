import subprocess
import os
from .errors import error


def checkdependencies():
    FNULL = open(os.devnull, "w")
    try:
        subprocess.run("unsquashfs", stdout=FNULL, stderr=FNULL)
    except:
        error(
            "unsquashfs program not found on this system, required for Isobox to function."
        )
