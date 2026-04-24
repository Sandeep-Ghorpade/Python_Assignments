# Train the model using only:
# StudyHours
# Attendance
# Compare the accuracy with the full-feature model.
# Is the model still performing well?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import(
    accuracy_score
)

DataPath = "edit_student_performance_ml.csv"
df = pd.read_csv(DataPath)

Border = "-" * 50
print(Border)

feature_cols = [
    "StudyHours",
    "Attendance"
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

# The new accuracy is 100 % after remove PreviousScore,AssignmentsCompleted,SleepHours columns 
# which is same before removing PreviousScore,AssignmentsCompleted,SleepHours columns
# The model still performing well after removing PreviousScore,AssignmentsCompleted,SleepHours columns.
