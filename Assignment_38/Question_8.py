# Create a plot showing relationship between AssignmentsCompleted and FinalResult.
# Explain your observation.

import pandas as pd
import matplotlib.pyplot as plt

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

passed = df[df["FinalResult"] == 1]
failed = df[df["FinalResult"] == 0]

plt.scatter(passed["AssignmentsCompleted"], passed["FinalResult"], color = "black", label = "Pass")
plt.scatter(failed["AssignmentsCompleted"], failed["FinalResult"], color = "yellow", label = "Fail")


plt.xlabel("AssignmnetsCompleted")
plt.ylabel("FinalResult")
plt.title("AssignmentsCompleted Vs FinalResult")
plt.legend()
plt.show()


# The plot shows that the student how has completed most assignment generally it is pass
# and student who has not solve more assignment are fail 
# In one point few students have solve same assignment but some are pass and some are failed then there result is depend upon other features(Ex - 5 assignment solve students)