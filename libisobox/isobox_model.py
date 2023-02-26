"""
The purpose of this class is to be serialized as json into /var/lib/isobox/isoboxes.json
It represents isobox entries
"""


class Isobox:
    def __init__(self, name, note, mountpoint):
        self.name = name
        self.note = note
        self.mountpoint = mountpoint
