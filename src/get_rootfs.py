import os


def get_rootfs():
    print("Looking for the iso's squashfs")
    for (root, dirs, files) in os.walk("/tmp/isobox_mount", topdown=True):
        if "filesystem.squashfs" in files:
            print(f"Iso's squashfs found! {root + '/filesystem.squashfs'}")
            return root + "/filesystem.squashfs"
