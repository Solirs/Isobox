from sh import unsquashfs, cd
import os
import shutil

def unsquash(mountpoint, squashedpath):
	if not os.path.exists(mountpoint):
		os.mkdir(mountpoint)
	cd(mountpoint)
	shutil.move("squashedpath", mountpoint)
	unsquashfs(mountpoint + "/" + os.path.basename(squashedpath))
	
