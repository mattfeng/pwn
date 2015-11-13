# General Procedures

1. Got a file? Don't know what it is?
  * <pre>file FILENAME</pre>
  * Really nice command that almost always works (besides truecrypt/veracrypt files).
2. Binwalk
  * <pre>binwalk</pre>
  * File carving and finding files embedded into other files.
3. Foremost
  * <pre>foremost</pre>
  * File carving and finding files embedded into other files.
4. Scalpel
  * <pre>scalpel</pre>
  * File carving and finding embedded files; not sure if this works very well.
5. Exiftool
  * Why not? Can't hurt
6. Directories, especially on LINUX
  * List all the files in the directory, including hidden ones.
    * <pre>ls -lah</pre>
  * List all the files, RECURSIVELY, and in a nice format
    * <pre>tree</pre>
7. Disk image?
  * Convert from VMDK to IMG/RAW, for easy mounting
8. strings strings string
  * <pre>strings FILE</pre>
  * <pre>strings -LEN FILE</pre>
  * <pre>strings FILE | grep TEXT</pre>
