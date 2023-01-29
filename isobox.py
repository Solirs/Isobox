import sys
import os
import argparse
import traceback
import json
from src.mnt import *
from src.get_rootfs import *
from src.unsquash_filesystem import *
from src.chroot import *
from src.filesystems import *
from src.isobox_model import Isobox
from src.getboxbyname import getboxbyname
from src.isroot import isroot


def create_required_files():  # Create files used by isobox like config files if they dont exist
    if not os.path.exists("/var/lib/isobox"):
        os.mkdir("/var/lib/isobox")
    if not os.path.exists("/var/lib/isobox/isoboxes.json"):
        with open("/var/lib/isobox/isoboxes.json", "w") as f:
            json.dump([], f)
    if not os.path.exists("/var/lib/isobox/mounts"):
        os.mkdir("/var/lib/isobox/mounts")


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="Command", dest="command")
    subparsers.required = True

    createparser = subparsers.add_parser("create", help="Create new isobox")
    createparser.add_argument("name")
    createparser.add_argument("isopath")

    createparser.add_argument("-mountpoint", type=str, default=None)

    runparser = subparsers.add_parser("run", help="Run existing isobox")
    runparser.add_argument("name")

    subparsers.add_parser("ls", help="List all isoboxes")

    guiparser = subparsers.add_parser("gui", help="Run existing isobox and start gui")
    guiparser.add_argument("name")
    guiparser.add_argument("-tty", type=str, default="3")

    return parser.parse_args()


def main(args):

    if os.getuid() != 0:
        sys.exit("Requires root")
    create_required_files()

    if args.command == "create":
        mountpoint = None

        if not args.mountpoint:
            mountpoint = f"/var/lib/isobox/mounts/{args.name}"
        else:
            mountpoint = args.mountpoint

        tempmount_iso(args.isopath)
        squashedpath = get_rootfs()
        unsquash(mountpoint, squashedpath)
        if not isroot(mountpoint):
            print(
                "No useable root in squashfs, looking for potential rootfs image file."
            )
            rootimg = find_rootimg(mountpoint)
            print(
                f"Potential rootfs image file found at {rootimg}, mounting it to /mnt!"
            )
            subprocess.run(f"mount -t auto {rootimg} /mnt".split())
            shutil.rmtree(mountpoint)

            print(f"Copying rootfs to {mountpoint}")
            for i in os.listdir("/mnt"):
                shutil.move(os.path.join("/mnt", i), mountpoint)

        with open("/var/lib/isobox/isoboxes.json", "r+") as f:
            boxeslist = json.load(f)

            newisobox = Isobox(name=args.name, note="", mountpoint=mountpoint)
            boxeslist.append(newisobox.__dict__)
            f.seek(0)
            f.write(json.dumps(boxeslist))
            f.truncate()

    elif args.command == "run":
        currentbox = getboxbyname(args.name)

        mount_filesystems(currentbox["mountpoint"])
        chroot(currentbox["mountpoint"])

        umount_filesystems(currentbox["mountpoint"])
    elif args.command == "gui":
        currentbox = getboxbyname(args.name)

        mount_filesystems(currentbox["mountpoint"])
        chroot_gui(currentbox["mountpoint"], args.tty)
        umount_filesystems(currentbox["mountpoint"])
    elif args.command in ("ls", "list"):
        boxeslist = None
        with open("/var/lib/isobox/isoboxes.json", "r+") as f:
            boxeslist = json.load(f)
        if len(boxeslist) == 0:
            sys.exit("No isoboxes on this system.")
        else:
            for i in boxeslist:
                print(i["name"])


if __name__ == "__main__":
    args = parse_args()

    try:
        main(args)
    except Exception as e:
        print(traceback.format_exc())
        umount_filesystems()
    except KeyboardInterrupt:
        umount_filesystems()
