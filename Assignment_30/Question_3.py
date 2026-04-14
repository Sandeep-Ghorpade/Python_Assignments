# Display File Line by Line
# Problem Statement:
# Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.

# Input:
# Demo.txt

# Expected Output:
# Display each line of Demo.txt one by one.

import sys

FileName = sys.argv[1]

with open(FileName, "r") as file:
    for line in file:
        print(line)
    
