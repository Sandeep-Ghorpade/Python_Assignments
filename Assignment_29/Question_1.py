# Check File Exists in Current Directory
# Problem Statement :
# Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

# Input:    
# Demo.txt

# Expected Output :   
# Display whether Demo.txt exists or not.

import os

FileName = input("Enter the filename : ")

if os.path.isfile(FileName):
    print(FileName," its exists")

else:
    print(FileName, "its not exists")