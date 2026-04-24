# Create a new DataFrame with details of 5 new students.
# Use the trained model to predict their results.
# Display predictions clearly.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    accuracy_score
)

DataPath = "student_performance_ml.csv"
df = pd.read_csv(DataPath)

Border = "-" * 50
print(Border)

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

Model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

Model.fit(X_train, Y_train)

print("Model train successfully")

print(Border)

Y_pred = Model.predict(X_test)

print("Model testing complete")

accuracy = accuracy_score(Y_pred, Y_test)

print(Border)

print("Accuracy of the model is : ",accuracy * 100)

data = [[6, 75, 50, 5, 6], [4.5, 60, 62, 4, 5], [3, 70, 85, 6, 7], [8.2, 80, 70, 5, 6], [5, 73, 69, 7, 8]]

result = Model.predict(data)

for i, value in enumerate(result):
    if value == 1:
        print(f"Student {i + 1} Pass")
    else:
        print(f"Student { i+ 1} Fail")

