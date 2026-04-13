import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('clean_titanic.csv')

X = df.drop("survived", axis=1)
y = df["survived"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

svm = SVC()
score = cross_val_score(svm, X=X_scaled, y=y, scoring='accuracy')
print(score)
print(score.mean())