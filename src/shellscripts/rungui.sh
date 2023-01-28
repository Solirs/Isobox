chroot $1 /bin/bash -c "chvt $2 && startx -- :$3 vt$2"
