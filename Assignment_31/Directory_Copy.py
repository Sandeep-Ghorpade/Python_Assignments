# Design automation script which accept two directory names. Copy all files from first directory into second directory.
# Second directory should be created at run time.
# Usage : DirectoryCopy.py “Demo” “Temp”

import sys
import os
import shutil

DirName = sys.argv[1]
NewDir = sys.argv[2]

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

shutil.copytree(DirName, NewDir)
print("New directory made successfully")