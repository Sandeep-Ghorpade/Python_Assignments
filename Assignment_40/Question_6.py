# Identify students where:
# y_test != y_pred
# Display those rows.
# How many students were misclassified?
# What common pattern do you observe?

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

accuracy = accuracy_score(Y_test, Y_pred)

print(Border)

print("Accuracy of the model is : ",accuracy * 100)

count = 0

for i in range(len(Y_test)):
    if (Y_test.iloc[i] != Y_pred[i]): # iloc[i] gives the value at position i 
        print("Misclassified student : ")
        print(X_test.iloc[i])
        print("Actual : ",Y_test.iloc[i],"Predicted : ",Y_pred[i])
        count = count + 1
print("Total misclassified student : ",count)





