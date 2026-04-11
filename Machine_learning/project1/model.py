import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


data = pd.read_csv('clean_insurance.csv')

# alloct X data and Y data
X = data.drop('charges',axis=1)
y = data['charges']

# Split data in train and test
X_train ,  X_test , y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train model
model = LinearRegression()
model.fit(X_train, y_train)

# prediction of model
y_pred = model.predict(X_test)

# Check  
r2score = r2_score(y_test, y_pred)
#                     (1 - R2)(n - 1) 
# adjusted R2 = 1 - -------------------
#                     n - P - 1
# n = no. of rows
# p = feature(columns)
n = X_test.shape[0]
p = X_test.shape[1]
adjusted_r2 = 1 -( ( 1 - r2score ) * ( n - 1) / ( n - p - 1))


print(int(r2score * 100))
print(int(adjusted_r2 * 100))