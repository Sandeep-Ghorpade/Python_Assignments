# Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of both files.

# If both files contain the same contents, display Success
# Otherwise display Failure

import filecmp
import sys

FileName1 = sys.argv[1]
FileName2 = sys.argv[2]

Result = filecmp.cmp(FileName1, FileName2)
if(Result == True):
    print("Display Success")
else:
    print("Display Failure")