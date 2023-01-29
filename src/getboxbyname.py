import json


def getboxbyname(name):
    with open("/var/lib/isobox/isoboxes.json", "r+") as f:
        boxeslist = json.load(f)
        return [i for i in boxeslist if i["name"] == name][0]
