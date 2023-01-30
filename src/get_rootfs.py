import os


def get_rootfs():
    print("Looking for the iso's squashfs")
    for (root, dirs, files) in os.walk(f"/tmp/isobox_mount/", topdown=True):
        for i in files:
            with open(root + "/" + i, "r") as f:
                bts = os.pread(f.fileno(), 4, 0)
                if bts.hex() == "68737173":

                    print(f"Iso's squashfs found! {root}/{i}")
                    return root + "/" + i


def find_rootimg(directory):
    for (root, dirs, files) in os.walk(directory, topdown=True):
        sfs = [i for i in files if i.endswith(".img") or i.startswith("root")]
        if sfs:
            return root + "/" + sfs[0]
