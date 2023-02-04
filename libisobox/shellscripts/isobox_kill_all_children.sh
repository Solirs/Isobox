#Kill the PIDs of all processes in the chroot but spare the PID that was passed as well as its parent process
#$1 Is likely to be the pid of the main session when isobox is started being passed when it is exited
#(See chroot.sh for example)
echo "Killing all processes in chroot..."
kill $(ps --format pid |grep -o "[0-9]*"|grep -wv $1|grep -wv $(ps -p $1 -o ppid=))

#DEPRECATED