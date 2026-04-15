# Design automation script which accept directory name and display checksum of all files.
# Usage : DirectoryChecksum.py “Demo”
# Demo is name of directory

import sys
import hashlib
import os

DirName = sys.argv[1]

for FolderName, SubFolder, FileName in os.walk(DirName):
    for fname in FileName:
        path = os.path.join(FolderName , fname)
        fobj = open(path, "rb")

        hobj = hashlib.md5()

        Buffer = fobj.read(1000)

        while(len(Buffer) > 0):
            hobj.update(Buffer)
            Buffer = fobj.read(1000)

        fobj.close()

        print(hobj.hexdigest())