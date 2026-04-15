# Design automation script which accept two directory names and one file extension.
# Copy all files with the specified extension from first directory into second directory. 
# Second directory should be created at run time.
# Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”

import sys
import os
import shutil

DirName = sys.argv[1]
NewDir = sys.argv[2]
Extension = sys.argv[3]

Ret = False

Ret = os.path.exists(DirName)
if(Ret == False):
    print("There is no such directory")

Ret = os.path.isdir(DirName)
if(Ret == False):
    print("It is not a directory")

if os.path.exists(NewDir):
    print("New directory already exists")
    exit()

os.mkdir(NewDir)

for FolderName, SubFolder, FileName in os.walk(DirName):
    for fname in FileName:
        ext = os.path.splitext(fname)[1]

        if ext == Extension:
            source = os.path.join(FolderName, fname)
            destinction = os.path.join(NewDir, fname)

            shutil.copy(source, destinction)

    print("New Directory is made successfully")
