## Run the latest KDE plasma with X11 on an isoboxed distro  
Here is a quick guide to run the latest KDE plasma desktop inside an isobox.  
For this example we will use the arch linux distribution as our guest and assume KDE plasma is installed on your system.  
This guide will pretty much work on every distro if the requirements are needed though.  

Before all pick a tty that's currently unused as well as a Xorg display that's also unused.  
You may also want to run  
`source /usr/local/bin/isobox_desktop_init.sh`  
To start stuff that you may want to have on a desktop like a sound server.

Then run the following: 

`startx /usr/bin/dbus-run-session startplasma-x11 -- :2 vt3`  
Replace ":2" with the display of your choosing and "vt3" with the tty of your choosing, (vt4) for example.  
Congratulations, you are now running the freshest KDE Plasma on Isobox.  

If you want to run plasma as a regular user without any config then the easy way is the following:  
Run the following as root  
`Xorg :2 vt3`  
Again, Replace ":2" with the display of your choosing and "vt3" with the tty of your choosing.
Then sudo into your user and run kde, for example:  
`sudo -u user bash`  
`DISPLAY=":2" dbus-run-session startplasma-x11`  

To run it through `isobox gui` you can add the command to your guest's xinitrc.  
`echo "dbus-run-session startplasma-x11" > /etc/X11/xinit/xinitrc`  
