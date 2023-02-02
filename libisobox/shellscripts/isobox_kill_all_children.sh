kill $(ps --format pid |grep -o "[0-9]*"|grep -wv $1|grep -wv $(ps -p $1 -o ppid=))
