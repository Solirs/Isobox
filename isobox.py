import sys
import os
from mnt import *
from get_rootfs import *


def main():
    if os.getuid() != 0:
        sys.exit("Requires root")
    path = sys.argv[1]
    tempmount_iso(path)
    get_rootfs()


main()
