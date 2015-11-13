# Virtual Machine

1. Identify the machine type
  * After downloading, match hashes to ensure file integrity (of the download)
  * <pre>md5sum
2. Make a pristine copy BEFORE extracting
3. Make a pristine copy AFTER extracting
4. Boot up the machine, and note the credentials used.
  * Single User Mode can bypass the login for some systems
5. Treat the virtual disks as if they were their own evidence; see the VMDK README.md
6. Things to look for
  * .bash_history
  * 'history' command
  * Installed programs (use google to find the command)
  * /tmp/VMwareDnD
  * .mozilla
    * Browsing history, cookies, etc
  * Of course, browse all the home directories
    * Desktop
    * Documents
    * Downloads
    * ...
7. Processes currently running
  * Find the currently running processes
    * <pre>ps -aux</pre>
  * Find the currently running connections, and their connected process
    * <pre>netstat -tulpn</pre>
8. Find processes that run on startup
  * 
