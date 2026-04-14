# Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.
# Input:
# Demo.txt Marvellous

# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt.

import sys

FileName = sys.argv[1]
String = sys.argv[2]

fobj = open(FileName,"r")

Data = fobj.read()
Frequency = Data.count(String)

print(Frequency)