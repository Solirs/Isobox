import os


def get_rootfs(dir=""):
    print("Looking for the iso's squashfs")
    for (root, dirs, files) in os.walk(f"/tmp/isobox_mount/{dir}", topdown=True):
        sfs = [i for i in files if i.endswith(".sfs") or i.endswith(".squashfs")]
        if sfs:

            print(f"Iso's squashfs found! {root}/{sfs[0]}")
            return root + "/" + sfs[0]
