# Photo Forensics
1. Standard stuff: open the image.
2. Extract the metadata off of the image
  <pre>exiftool FILENAME</pre>
3. Run stegdetect on it
  * Hard to install; get this working before the competition (at least one person...)
4. Run steghide on it
  * Software preferred by NYU-Poly, so if there's something suspicious, use this!
5. Outguess, perhaps
  * Outguess was used in Cicada 3301, don't know if it has any relevance here.
6. Photo Recovery
  * File headers, always
  * Google the structure of a PNG file if needed
7. Note if the image appears to be cut or corrupted
  * This means that either the owner was messing with the image, or the device he was using corrupted
