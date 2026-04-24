# Train model using:
# random_state = 0
# random_state = 10
# random_state = 42
# Compare testing accuracy.
# Does the result change?

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
    random_state=10
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


# The accuracy changes in random state 0 the accuracy is 83.33 %, in random state 10 its same 83.33 % when i change random state to 42 the accuracy becomes 100%.
# When i observe the output in random state 0 and 10 the tricy row is in test set 
# In random state 42 the tricy row is in training set 
# Thats the reason behind the accuracy.




