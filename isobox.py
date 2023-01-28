import sys
import os
from src.mnt import *
from src.get_rootfs import *
from src.unsquash_filesystem import *
from src.chroot import chroot
import argparse
from src.filesystems import *


def create_required_files():  # Create files used by isobox like config files if they dont exist
    if not os.path.exists("/var/lib/isobox"):
        os.mkdir("/var/lib/isobox")


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="Command", dest="command")
    subparsers.required = True
    createparser = subparsers.add_parser("create", help="Create new isobox")
    runparser = subparsers.add_parser("run", help="Run existing isobox")
    guiparser = subparsers.add_parser("gui", help="Run existing isobox and start gui")
    return parser.parse_args()


def main():

    args = parse_args()
    if os.getuid() != 0:
        sys.exit("Requires root")
    create_required_files()

    if args.command == "create":
        tempmount_iso(path)
        squashedpath = get_rootfs()
        unsquash("/mnt/debian", squashedpath)
    elif args.command in ("run", "gui"):
        mount_filesystems()
        chroot("/mnt/debian")
        umount_filesystems()


main()
