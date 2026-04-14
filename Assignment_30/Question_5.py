# Search a Word in File

# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.

# Input:
# Demo.txt Marvellous

# Expected Output:
# Display whether the word Marvellous is found in Demo.txt or not.

import sys

FileName = sys.argv[1]
WordName = sys.argv[2]

with open(FileName, "r") as file:
    Data = file.read()

if WordName in Data:
    print(WordName,"word is present in the file")
else:
    print(WordName,"word is not present in the file")

