## Isobox
Isobox is a command line program that allows to run a full linux system from an iso file in a chroot jail alongside one's system.
You can even run a graphical shell/desktop environment inside it, though it may or may not require some intervention depending on the guest system and desktop environment.

### Disclaimer:
  Isobox exposes a lot of stuff to its chroot jails, including devices.
  It is therefore NOT recommended to use if any sort of security is in play.
  
  It is also pretty much in Alpha at the moment, dont expect too much polishing or features.
  Some systems will not work, but i've tested most major distributions with good results.

### Requirements:
  A python interpreter
  The `unsquashfs` utility
  A linux system
  
  
  

![Screenshot](https://i.imgur.com/rX7YgGI.png)