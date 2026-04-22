# Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain.

import pandas as pd
import matplotlib.pyplot as plt

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

passed = df[df["FinalResult"] == 1]
failed = df[df["FinalResult"] == 0]

plt.scatter(passed["SleepHours"], passed["FinalResult"], color = "black", label = "Pass")
plt.scatter(failed["SleepHours"], failed["FinalResult"], color = "yellow", label = "Fail")


plt.xlabel("SleepHours")
plt.ylabel("FinalResult")
plt.title("SleepHours Vs FinalResult")
plt.legend()
plt.show()


# The plot shows that sleeping more not guarantee success because few students sleep same hours some are pass and some are failed(ex - 6 hours)