# Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer.

import pandas as pd

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

Total = len(df)

counts = df["FinalResult"].value_counts()

passed = counts[1]
failed = counts[0]

passed_percentage = passed/Total * 100
failed_percentage = failed/Total * 100

print("Total passed student :",passed_percentage,"%")
print("Total failed student :",failed_percentage,"%")

# Dataset is imbalanced because total passed student is 60.0 % and total failed student is 40.0 %

