# Copy File Contents into Another File

# Problem Statement:
# Write a program which accepts two file names from the user.
# First file is an existing file
# Second file is a new file

# Copy all contents from the first file into the second file.

# Input:
# ABC.txt Demo.txt

# Expected Output:
# Contents of ABC.txt copied into Demo.txt.

import sys
import shutil

ExistingFileName = sys.argv[1]
NewFileName = sys.argv[2]

if shutil.copy(ExistingFileName, NewFileName):
    print("Contents of existing file is copied into new file")
else:
    print("Contents are not copied from existing file into new file")


