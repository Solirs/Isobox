import json
import sys


def list_isoboxes():
    boxeslist = None
    with open("/var/lib/isobox/isoboxes.json", "r+") as f:
        boxeslist = json.load(f)
    if len(boxeslist) == 0:
        sys.exit("No isoboxes on this system.")
    else:
        for i in boxeslist:
            print(i["name"])
