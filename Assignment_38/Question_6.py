# Create a scatter plot of:
# StudyHours vs PreviousScore

import pandas as pd
import matplotlib.pyplot as plt

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

passed = df[df["FinalResult"] == 1]
failed = df[df["FinalResult"] == 0]

plt.scatter(passed["StudyHours"], passed["PreviousScore"], color = "black", label = "Pass")
plt.scatter(failed["StudyHours"], failed["PreviousScore"], color = "yellow", label = "Fail")


plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.title("StudyHours vs PreviousScore")
plt.legend()
plt.show()

