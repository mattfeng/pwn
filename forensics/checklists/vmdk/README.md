# Virtual Hard Disk

1. Convert to RAW/IMG
  * Might to join the files together
  * <pre>qemu-img convert -f vmdk -O raw FILE.vmdk FILE.raw</pre>
2. Load the image into FTK Imager
3. Mount the file in Kali using
  * <pre>mount FILE.raw /MOUNTPOINT</pre>
  * Capitals mean replace with the actual file and mountpoint.
4. Look at the root directory for interesting files
  * <pre>cd /</pre>
  * <pre>ls -la</pre>
  * Some directories are default, and some are not. Common defaults are
    * /bin
    * /boot
    * /dev
    * /etc
    * /home
    * /lib
    * /lost+found
    * /mnt
    * /mount
    * /opt
    * /root
    * /proc (all the running processes)
    * /tmp (might some interesting info)
    * /usr
    * /var (log files are located here)
  * That isn't to say don't look for evidence in those directories!
5. If prefered, you can mount the drive directly into Kali for analysis.
  * Seungkyoon's computer
6. Log files
  * /var/log
