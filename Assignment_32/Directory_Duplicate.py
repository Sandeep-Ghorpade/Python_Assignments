# Design automation script which accept directory name and write names of duplicate files from
# that directory into log file named as Log.txt. Log.txt file should be created into current directory.
# Usage : DirectoryDuplicate.py “Demo”

import sys
import hashlib
import os

DirName = sys.argv[1]

files = []
checksum = []

for FolderName, SubFolder, FileName in os.walk(DirName):
    for fname in FileName:
        path = os.path.join(FolderName , fname)

        files.append(path)

        with open(path, "rb") as fobj:
            hobj = hashlib.md5()
            Buffer = fobj.read(1000)

            while(len(Buffer) > 0):
                hobj.update(Buffer)
                Buffer = fobj.read(1000)

        checksum.append(hobj.hexdigest())

with open("Log.txt","w") as log:
    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            if (checksum[i] == checksum[j]):
                log.write(files[j] + "\n")
        