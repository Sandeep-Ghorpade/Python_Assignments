# Count Lines in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.

# Input:
# Demo.txt

# Expected Output:
# Total number of lines in Demo.txt

import sys

FileName = sys.argv[1]

count = 0

with open(FileName, "r") as file:
    for line in file:
        count = count + 1;

print("Total lines in the file is : ",count)