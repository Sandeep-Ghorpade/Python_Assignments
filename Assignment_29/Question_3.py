# Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, 
# and copies all contents from the given file into Demo.txt.

# Input (Command Line):
# ABC.txt

# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import sys
import shutil

ExistingFileName = sys.argv[1]

shutil.copy(ExistingFileName, "Demo.txt")
print("File gets successfully copied")

