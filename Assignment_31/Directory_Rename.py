# Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion.
# Usage : DirectoryRename.py “Demo” “.txt” “.doc”

import sys
import os

DirName = sys.argv[1]
Extension1 = sys.argv[2]
Extension2 = sys.argv[3]

Ret = False

Ret = os.path.exists(DirName)
if(Ret == False):
    print("There is no such directory")

Ret = os.path.isdir(DirName)
if(Ret == False):
    print("It is not a directory")

for FolderName, SubFolder, FileName in os.walk(DirName):
    for fname in FileName:
        ext = os.path.splitext(fname)[1]

        if(ext == Extension1):
            Name = os.path.splitext(fname)[0]

            NewName = Name + Extension2

            OldPath = os.path.join(FolderName, fname)
            NewPath = os.path.join(FolderName, NewName)

            os.rename(OldPath, NewPath)

            print(NewName) 