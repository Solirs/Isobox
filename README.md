## Isobox
Isobox is a command line program that allows to run a full linux system from an iso file in a chroot jail alongside one's system.
You can even run a graphical shell/desktop environment inside it, though it may or may not require some intervention depending on the guest system and desktop environment.

### Disclaimer:
  Isobox exposes a lot of stuff to its chroot jails, including devices.
  It is therefore NOT recommended to use if any sort of security is in play.
  
  It is also pretty much in Alpha at the moment, dont expect too much polishing or features.
  Some systems will not work, but i've tested most major distributions (Arch, Debian, Fedora, Ubuntu flavours like xubuntu and linux mint) and some lesser   known distros (Void, Endeavour OS) with good results.

### But why?:
  - To be able to get into a disposable system in 2 commands and a few seconds
  - To test out distros without booting them
  - To be able to do dangerous or distro specific stuff in a semi-isolated environment.
  - Because having a second separate ready to use environment is always good for activities needing a lot of programs like pentesting
  - For fun and practice

### Requirements:
  A python interpreter  
  The `unsquashfs` utility  
  A linux system  
  
  
  

![Screenshot](https://i.imgur.com/rX7YgGI.png)
