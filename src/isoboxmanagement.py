import json
import sys
from .errors import error


def getboxbyname(name):
    with open("/var/lib/isobox/isoboxes.json", "r+") as f:
        boxeslist = json.load(f)
        results = [i for i in boxeslist if i["name"] == name]
        if results:
            return results[0]
        else:
            error("The Isobox you're refering to does not exist.")
