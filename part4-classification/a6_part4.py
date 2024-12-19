import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Print the values for x and y
print("X:")
print(x)
print("\goal Y:")
print(y)
# Step 2: Standardize the data using StandardScaler, 
scale=StandardScaler().fit(x)
x=scale.transform(x)
# Step 3: Transform the data
x=scale.transform(x)
# Step 4: Split the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
# Step 6: Create a LogsiticRegression object and fit the data
modelone=linear_model.LogisticRegression().fit(x_train,y_train)
# Step 7: Print the score to see the accuracy of the model
acurate=modelone.score(x_test,y_test)
# Step 8: Print out the actual ytest values and predicted y values
# based on the xtest data
print("acurracy=",acurate )
print("test results=")
print("")
for index in range(len(x_test)):
    # Predict gender based on test features
    x_sample = x_test[index].reshape(1, 3)  # Ensuring it's in the correct shape (1, 3)
    y_pred = int(modelone.predict(x_sample))  # Predict the value (0 or 1)
    print(x)
    # Map predicted value to "Male" or "Female"
    y_pred_label = "Male" if y_pred == 0 else "Female"
    
    # Actual value
    actual = y_test[index]
    actual_label = "Male" if actual == 0 else "Female"
    
    # Print predicted and actual values
    print(f"Predicted Gender: {y_pred_label} | Actual Gender: {actual_label}")
    print("")