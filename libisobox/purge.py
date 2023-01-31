import json
import shutil


def purge():
    with open("/var/lib/isobox/isoboxes.json", "r") as f:
        boxeslist = json.load(f)
        for i in boxeslist:
            print(f"Deleting root for isobox {i['name']} at {i['mountpoint']}")
            shutil.rmtree(i["mountpoint"])
            print(f"Done deleting root for isobox {i['name']}")

    print("Deleting /var/lib/isobox")
    shutil.rmtree("/var/lib/isobox")

    print("Done")
