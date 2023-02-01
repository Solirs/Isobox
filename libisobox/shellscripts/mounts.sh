SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd ) #Get script directory

cp "$SCRIPT_DIR/isobox_desktop_init.sh" "$1/usr/local/bin/isobox_desktop_init.sh"
mount -t proc /proc $1/proc
mount -o bind /dev $1/dev
mount -o bind /dev/pts $1/dev/pts
mount -o bind /run $1/run
mount -o bind /tmp $1/tmp
mount -t sysfs /sys $1/sys
cp -r /etc/resolv.conf $1/etc/resolv.conf
