# Write a program to:
#    Display total number of students in the dataset
#    Count how many students Passed (FinalResult = 1)
#    Count how many students Failed (FinalResult = 0)

import pandas as pd

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

totalstudents = len(df)
print("Total number of students in the dataset are :",totalstudents)

passed = (df["FinalResult"] == 1).sum()
print("Total students passed are:",passed)

failed = (df["FinalResult"] == 0).sum()
print("Total failed students are : ",failed)