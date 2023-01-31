import sys
import os
import argparse
import traceback
import json
from src.mnt import *
from src.rootfs import *
from src.unsquash_filesystem import *
from src.chroot import *
from src.filesystems import *
from src.isobox_model import Isobox
from src.isoboxmanagement import getboxbyname
from src.checkdependencies import checkdependencies


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

    removeparser = subparsers.add_parser("remove", help="Remove existing isobox")
    removeparser.add_argument("name")

    infoparser = subparsers.add_parser("info", help="Print info about an isobox")
    infoparser.add_argument("name")

    mvparser = subparsers.add_parser(
        "move", help="Move an isobox to another directory on your system."
    )
    mvparser.add_argument("name")
    mvparser.add_argument("target")

    createparser.add_argument("-mountpoint", type=str, default=None)

    runparser = subparsers.add_parser(
        "shell", help="Gain a shell into an existing isobox"
    )
    runparser.add_argument("name")

    subparsers.add_parser("ls", help="List all isoboxes")

    guiparser = subparsers.add_parser("gui", help="Run existing isobox and start gui")
    guiparser.add_argument("name")
    guiparser.add_argument("-tty", type=str, default="3", help="The tty to startx into")
    guiparser.add_argument(
        "-display",
        type=str,
        default="2",
        help="The display to start the Xorg server on",
    )
    return parser.parse_args()


def main(args):

    create_required_files()

    if args.command == "create":
        isopath = os.path.abspath(args.isopath)
        mountpoint = None

        if not args.mountpoint:
            mountpoint = f"/var/lib/isobox/mounts/{args.name}"
        else:
            mountpoint = args.mountpoint

        tempmount_iso(isopath)
        try:
            squashedpath = get_rootfs()
            unsquash(mountpoint, squashedpath)
        finally:
            subprocess.run(["umount", "/tmp/isobox_mount"])

        if not isroot(
            mountpoint
        ):  # Sometimes distributions leave an img file of the root filesystem in the squashfs, we need to handle that
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

            subprocess.run(f"cp -R /mnt {mountpoint}".split())
            subprocess.run(f"umount /mnt".split())

        with open("/var/lib/isobox/isoboxes.json", "r+") as f:
            boxeslist = json.load(f)

            newisobox = Isobox(name=args.name, note="", mountpoint=mountpoint)
            boxeslist.append(newisobox.__dict__)
            f.seek(0)
            f.write(json.dumps(boxeslist))
            f.truncate()

    elif args.command == "shell":
        currentbox = getboxbyname(args.name)

        mount_filesystems(currentbox["mountpoint"])
        chroot(currentbox["mountpoint"])

        umount_filesystems(currentbox["mountpoint"])
    elif args.command == "gui":
        currentbox = getboxbyname(args.name)

        mount_filesystems(currentbox["mountpoint"])
        chroot_gui(currentbox["mountpoint"], args.tty, args.display)
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
    elif args.command == "remove":
        currentbox = getboxbyname(args.name)
        print(f"Deleting isobox {args.name}")
        shutil.rmtree(currentbox["mountpoint"])

        with open("/var/lib/isobox/isoboxes.json", "r+") as f:
            boxeslist = json.load(f)
            toremove = [i for i in boxeslist if i["name"] == args.name]

            boxeslist[:] = [i for i in boxeslist if i["name"] != args.name]
            f.seek(0)
            f.write(json.dumps(boxeslist))
            f.truncate()
    elif args.command == "move":
        currentbox = getboxbyname(args.name)
        currentmountpoint = currentbox["mountpoint"]
        target = os.path.abspath(args.target)

        subprocess.run(f"mv {currentmountpoint}/* {target}", shell=True)

        with open("/var/lib/isobox/isoboxes.json", "r+") as f:
            boxeslist = json.load(f)
            tomove = [i for i in boxeslist if i["name"] == args.name][0]
            tomove["mountpoint"] = target
            f.seek(0)
            f.write(json.dumps(boxeslist))
            f.truncate()
    elif args.command == "info":
        currentbox = getboxbyname(args.name)
        print(f"Info about box {currentbox['name']}:\n")
        print(f"Name: {currentbox['name']}")
        print(f"Mountpoint: {currentbox['mountpoint']}")
        print(f"Note: {currentbox['note']}")


if __name__ == "__main__":

    if (
        os.getuid() != 0
    ):  # Quit if user is not root as root is pretty much required for this to run properly
        sys.exit("Requires root")
    checkdependencies()  # Check if unsquashfs is installed basically

    args = parse_args()
    currentmountpoint = None
    # Set the currentmountpoint here so we can unmount mounted filesystems  here if something goes south
    if args.command in ("shell", "gui") and getboxbyname(args.name):
        currentmountpoint = getboxbyname(args.name)["mountpoint"]

    try:
        main(args)
    except Exception as e:
        print(traceback.format_exc())
        if args.command in ("shell", "gui"):
            umount_filesystems(currentmountpoint)
    except KeyboardInterrupt:
        if args.command in ("shell", "gui"):
            umount_filesystems(currentmountpoint)
