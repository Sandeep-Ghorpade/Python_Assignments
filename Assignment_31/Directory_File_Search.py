# Design automation script which accept directory name and file extension from user. Display all files with that extension.
# Usage : DirectoryFileSearch.py “Demo” “.txt”

import sys
import os

DirName = sys.argv[1]
Extension = sys.argv[2]

Ret = False

Ret = os.path.exists(DirName)
if(Ret == False):
    print("There is no such directory")

Ret = os.path.isdir(DirName)
if(Ret == False):
    print("It is not a directory")

for FolderName, SubFolder, FileName in os.walk(DirName):
    for fname in FileName:
        ext = os.path.splitext(fname)[1] # splitexe -> seperate filename and extension # [1] -> Gives the second element means extension

        if(Extension == ext):
            print(fname)