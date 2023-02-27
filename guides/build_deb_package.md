## Setup a Debian packaging environment and build a Debian package inside an isoboxed Debian install.

Before all you will need a fully functionning Debian isobox.  
For the example i use the debian-live-11.6.0-amd64-standard.iso iso file that can  
be found in your favourite Debian mirro under debian-cd/11.6.0-live/amd64/iso-hybrid/.  
We will be using Debian 11 bullseye in this guide.  
A hashtag before a command means it must run as root.  
A dollar sign means it mustt run as a regular user. 

You can then create it by running something like:  
`# isobox create debian path_to_debian_iso`  
And chroot inside it with:  
`# isobox shell debian`  

You are now inside a fully functionning debian chroot, let's get to building our package!  
For this example we will rebuild the `ksh` package.  

First of all install the `build-essential` and `devscripts` packages.  
`# apt install build-essential`  
`# apt install devscripts`  
(If you get an error about the statoverride file, delete /var/lib/dpkg/statoverride and run `dpkg --configure -a`)  

Then add the deb-src stuff into /etc/apt/sources.list.  
In this iso you can do that by uncommenting the line `deb-src http://deb.debian.org/debian/ bullseye main` in  /etc/apt/sources.list and running `# apt update`.  

Next up install the build dependencies of the `ksh` package.  
`# apt build-dep ksh`  

From this point onwards you should be following the instructions as a regular user and not root.  
Pick a user inside your host environment, create a /home for it and chown it to the user.  
`# mkdir /home/user`  
`# chown -R user /home/user`

Then gain a shell as that user  
`# sudo -u user bash`
`$ cd ~`  


Make yourself a cozy directory somewhere.  
`$ mkdir ~/ksh`  

And grab the source package of ksh.  
`$ apt source ksh`  

Quite a few files will sneak into your ~/ksh , we are interested by the single directory that was created.
Cd into it:  
`$ cd ksh-*`  

You can now start building the package and grab a coffee.  
`$ debuild -us -uc`  
(Remove the -us and -uc flags to enable GPG signing.)

Once your package is done building cd into the ~/ksh directory once again.  
You should find two new deb packages. ksh-dgbsym*.deb and ksh_*.deb.  
Simply install the ksh_*.deb one:  
`# dpkg -i ksh_*.deb`  
And run `ksh` to check if everything went right

Congratulations you have built a Debian package with the help of Isobox.  


![](https://i.imgur.com/xaNRXNJ.png)  


Special thanks to this document which was useful in the making of this guide:  
https://www.debian.org/doc/manuals/packaging-tutorial/packaging-tutorial.en.pdf     