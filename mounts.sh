
mount -t proc /proc /mnt/debian/proc
mount -o bind /dev /mnt/debian/dev
mount -o bind /dev/pts /mnt/debian/dev/pts
mount -o bind /run /mnt/debian/run
mount -o bind /tmp /mnt/debian/tmp
mount -t sysfs /sys /mnt/debian/sys
cp /run/user/1000/gdm/Xauthority /mnt/debian/root/.Xauthority
