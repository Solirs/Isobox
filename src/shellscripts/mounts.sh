
mount -t proc /proc $1/proc
mount -o bind /dev $1/dev
mount -o bind /dev/pts $1/dev/pts
mount -o bind /run $1/run
mount -o bind /tmp $1/tmp
mount -t sysfs /sys $1/sys
cp /run/user/1000/gdm/Xauthority $1/root/.Xauthority
