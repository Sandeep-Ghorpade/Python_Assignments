# Display File Contents
# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.

# Input:
# Demo.txt

# Expected Output:
# Display contents of Demo.txt on console.

import os

FileName = input("Enter filename : ")

fobj = open(FileName,"r")

Data = fobj.read()
print(Data)