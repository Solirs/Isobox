import os


def get_rootfs():
    print("Looking for the iso's squashfs")
    for (root, dirs, files) in os.walk(f"/tmp/isobox_mount/", topdown=True):
        sfs = [
            i
            for i in files
            if i.endswith(".sfs") or i.endswith(".squashfs") or i.startswith("squashfs")
        ]
        if sfs:

            print(f"Iso's squashfs found! {root}/{sfs[0]}")
            return root + "/" + sfs[0]


def find_rootimg(directory):
    for (root, dirs, files) in os.walk(directory, topdown=True):
        sfs = [i for i in files if i.endswith(".img") or i.startswith("root")]
        if sfs:
            return root + "/" + sfs[0]
