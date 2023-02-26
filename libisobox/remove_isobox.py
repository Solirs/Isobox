import json
import shutil
from .isoboxmanagement import getboxbyname


def remove_isobox(args):
    currentbox = getboxbyname(args.name)
    print(f"Deleting isobox {args.name}")
    try:
        shutil.rmtree(currentbox["mountpoint"])
    except FileNotFoundError:
        pass
    finally:
        print(f"Deleting entry for isobox {args.name}")

        with open("/var/lib/isobox/isoboxes.json", "r+") as f:
            boxeslist = json.load(f)
            toremove = [i for i in boxeslist if i["name"] == args.name]

            boxeslist[:] = [i for i in boxeslist if i["name"] != args.name]
            f.seek(0)
            f.write(json.dumps(boxeslist))
            f.truncate()
