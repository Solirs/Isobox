"""
This file contains the code related to handling process signals such as SIGTERM to gracefully 
end the program
"""

import signal
from .cleanup_processes import cleanup_processes
from .filesystems import umount_filesystems


class Signalhandler:
    def __init__(self, currentmountpoint):
        self.mountpoint = currentmountpoint
        self.dead = False
        signal.signal(signal.SIGINT, self.handle_kill)
        signal.signal(signal.SIGTERM, self.handle_kill)

    def handle_kill(self, *args):
        print("Isobox is being killed, exiting peacefully...")
        self.dead = True
        umount_filesystems(self.mountpoint)
        cleanup_processes(self.mountpoint)
