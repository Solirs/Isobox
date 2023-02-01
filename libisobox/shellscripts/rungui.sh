


chroot $1 /bin/bash -c "bash /usr/local/bin/isobox_desktop_init.sh & chvt $2 && startx -- :$3 vt$2"