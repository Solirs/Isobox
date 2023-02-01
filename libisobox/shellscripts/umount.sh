
umount -f -l $1/proc
umount -f -l $1/dev
umount -f -l $1/run
umount -f -l $1/tmp
umount -f -l $1/sys

rm "$1/usr/local/bin/isobox_desktop_init.sh" 