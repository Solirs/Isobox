
chroot $1 /usr/bin/bash -c 'trap "bash /usr/local/bin/isobox_kill_all_children.sh $PPID" EXIT && bash'