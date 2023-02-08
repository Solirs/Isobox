umount `grep $1 /proc/mounts | cut -f2 -d" " | sort -r`

rm "$1/usr/local/bin/isobox_desktop_init.sh" 