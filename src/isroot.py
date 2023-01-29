import os


def isroot(path):
    if (
        os.path.exists(path + "/boot")
        and os.path.exists(path + "/dev")
        and os.path.exists(path + "/usr")
    ):
        return True

    return False
