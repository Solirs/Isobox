import json
import subprocess
import os

from .rootfs import get_rootfs, find_rootimg, isroot
from .isobox_model import Isobox
from .mnt import tempmount_iso
from .unsquash_filesystem import unsquash
import shutil


def create_isobox(args):
    isopath = os.path.abspath(args.isopath)
    mountpoint = None

    if not args.mountpoint:
        mountpoint = f"/var/lib/isobox/mounts/{args.name}"
    else:
        mountpoint = args.mountpoint

    tempmount_iso(isopath)
    try:
        squashedpath = None
        if args.sfspath:
            squashedpath = "/tmp/isobox_mount/" + args.sfspath
        else:
            squashedpath = get_rootfs()
        unsquash(mountpoint, squashedpath)
    finally:
        subprocess.run(["umount", "/tmp/isobox_mount"])

    if not isroot(
        mountpoint
    ):  # Sometimes distributions leave an img file of the root filesystem in the squashfs, we need to handle that
        print("No useable root in squashfs, looking for potential rootfs image file.")
        rootimg = find_rootimg(mountpoint)
        print(f"Potential rootfs image file found at {rootimg}, mounting it to /mnt!")
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

    rootpath = mountpoint + "/root/"

    userhomes = os.listdir(mountpoint + "/home")
    userhomes = [
        i
        for i in userhomes
        if not i.startswith(".") and ".config" in os.listdir(mountpoint + "/home/" + i)
    ]

    if len(userhomes) == 1 and os.path.exists(
        mountpoint + "/home/" + "/" + userhomes[0]
    ):
        print("Found user in iso's root...")
        configpath = mountpoint + "/home/" + "/" + userhomes[0] + "/.config"
        answer = input(
            f"A user's home directory was found on the live system at /home/{userhomes[0]} would you like to copy this user's .config to the /root directory? It may be necessary in order to have the distro's custom desktop environment config when entering the gui [Y/N]: "
        ).lower()
        if answer in ("y", "yes"):
            if os.path.exists(rootpath + "/.config"):
                shutil.rmtree(rootpath + "/.config")
            subprocess.run(f"cp -R {configpath} {rootpath}".split())
            print("Done!")
    elif len(userhomes) > 1:
        x = 1
        for i in userhomes:
            print(f"{x}: {'/home/' + i}")
            x += 1
        answer = input(
            "Several user homes were found in the iso, do you want to copy the .config of one of them to the root directory? It may be useful to have some of the distro's config like the desktop environment customizations. (number/n):"
        ).lower()
        if answer.isdigit():
            userhome = userhomes[int(answer) - 1]
            configpath = mountpoint + "/home/" + userhome + "/.config"
            if os.path.exists(rootpath + "/.config"):
                shutil.rmtree(rootpath + "/.config")
            subprocess.run(f"cp -R {configpath} {rootpath}".split())
            print("Done!")
