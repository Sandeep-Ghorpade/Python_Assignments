# Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.

# Input:
# Demo.txt

# Expected Output:
# Total number of words in Demo.txt.

import sys

FileName = sys.argv[1]

count = 0

with open(FileName, "r") as file:
    for line in file:
        words = line.split()
        count = count + len(words)

print("Total numbers of words in file is : ",count)
