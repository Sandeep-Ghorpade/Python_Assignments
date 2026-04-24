# Without using accuracy_score, manually calculate accuracy:
# Verify whether it matches sklearn accuracy.

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

correct = 0

for actual, pred in zip(Y_test, Y_pred):
    if actual == pred:
        correct = correct + 1;

manual_accuracy = correct/len(Y_test)

print("Manual accuracy is : ",manual_accuracy * 100)



