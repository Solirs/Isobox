# Isobox usage guide
Isobox "containers" are referred to as "isoboxes" or an "isobox"
Isobox as a program is referred to as Isobox with a capital I (except in commands).

In order to create an isobox you first need a distro's iso, for this example we will use  
the iso you can find at https://sourceforge.net/projects/mx-linux/files/Final/Xfce/MX-21.3_x64.iso/download

Once you have your iso, you'll have to create an isobox for it.
The command is the following:  
`isobox create name path-to-iso`  
name and path-to-iso being positional arguments.

This will find the squashfs in the iso, and unsquash it into /var/lib/isobox/mounts/name or the mountpoint  
specified with the -mountpoint argument.

Congratulations! You made your first isobox.
Next up you can do several things.

Firstly gain a root shell into that isobox with the command:  
`isobox shell name`  

Secondly, you can try to make Isobox attempt to startx inside the isobox  
potentially launching the live iso's gui, it doesnt work all the time, but it can do the trick.:  
`isobox gui name`  
You may want to set the -tty argument to launch the gui in another tty.  
Or the -display argument to set the display to startx on (:0, :1, :2, etc). 

You now know the basics of Isobox! There are more commands like `isobox ls` that you can discover and that arent covered here, but you can now use Isobox.  

