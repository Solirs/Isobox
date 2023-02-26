import json
import shutil
from .isoboxmanagement import getboxbyname
import os
import subprocess


def move_isobox(args):
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
