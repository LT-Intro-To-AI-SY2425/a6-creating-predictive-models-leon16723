import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)

# Create the model

# Fin the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 


# Print out the linear equation and r squared value

# Predict the the blood pressure of someone who is 43 years old.
# Print out the prediction

# Create the model in matplotlib and include the line of best fit

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values


x = x.reshape(-1,1)

model = LinearRegression()
model.fit(x, y)

slope = round(model.coef_[0], 2)
intercept = round(model.intercept_, 2)
r_squared = round(model.score(x, y), 2)

print(f"Linear equation: y = {slope}x + {intercept}")
print(f"R-squared value: {r_squared}")

age = np.array([[43]])  
prediction = model.predict(age)
print(f"Predicted blood pressure for someone who is 43 years old: {prediction[0]}")

plt.scatter(x, y, color="blue", label="Data points")
plt.plot(x, model.predict(x), color="red", label="Line of best fit")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Age vs Blood Pressure")
plt.legend()
plt.show()