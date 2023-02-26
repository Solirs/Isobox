import os


# This function looks into every file in the iso and checks if it is a squashfs
# If it is it returns the squashfs's path.
def get_rootfs():
    print("Looking for the iso's squashfs")
    for (root, dirs, files) in os.walk(f"/tmp/isobox_mount/", topdown=True):
        for i in files:
            with open(root + "/" + i, "r") as f:
                # Check if file is a squashfs
                bts = os.pread(f.fileno(), 4, 0)
                if bts.hex() == "68737173":

                    print(f"Iso's squashfs found! {root}/{i}")
                    return root + "/" + i


# This function finds rootfs.img which may be stored into the squashfs for some isos
def find_rootimg(directory):
    for (root, dirs, files) in os.walk(directory, topdown=True):
        sfs = [i for i in files if i.endswith(".img") or i.startswith("root")]
        if sfs:
            return root + "/" + sfs[0]


def isroot(path):
    if (
        os.path.exists(path + "/boot")
        and os.path.exists(path + "/dev")
        and os.path.exists(path + "/usr")
    ):
        return True

    return False
