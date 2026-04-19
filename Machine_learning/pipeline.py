import pandas as pd
from sklearn.preprocessing import RobustScaler , OneHotEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Step 1: Load & Quick Clean
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df  = pd.read_csv(url)
df.to_csv('git_titanic.csv', encoding='utf-8', index=False)
df.drop(['PassengerId','Name','Ticket','Cabin'],
        axis=1, inplace=True)

X = df.drop('Survived', axis=1)
y = df['Survived']

# Step 2: Define columns
numeric_cols     = ['Age','Fare','SibSp','Parch']
categorical_cols = ['Sex','Embarked','Pclass']

# Step 3: Build pipelines
num_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler',  RobustScaler())
])

cat_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore',
                              sparse_output=False))
])

# Step 4: Combine
preprocessor = ColumnTransformer([
    ('num', num_pipe, numeric_cols),
    ('cat', cat_pipe, categorical_cols)
])

# Step 5: Final pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestClassifier(
                n_estimators=100, random_state=42))
])

# Step 6: Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 7: Train
pipeline.fit(X_train, y_train)

# Step 8: Evaluate
y_pred = pipeline.predict(X_test)
print(f"Test Accuracy : {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred,
      target_names=['Died','Survived']))

# Step 9: Cross validate
cv_scores = cross_val_score(pipeline, X, y, cv=5)
print(f"\nCV Mean : {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

# Step 10: Save pipeline
import joblib
joblib.dump(pipeline, 'titanic_pipeline.pkl')
print("\n✅ Pipeline saved to titanic_pipeline.pkl")

# Step 11: Load & predict new data
loaded_pipe = joblib.load('titanic_pipeline.pkl')
new_passenger = pd.DataFrame([{
    'Pclass': 3, 'Sex': 'male', 'Age': 25,
    'SibSp': 0, 'Parch': 0,
    'Fare': 7.5, 'Embarked': 'S'
}])
prediction = loaded_pipe.predict(new_passenger)
print(f"\nNew Passenger Prediction: {'Survived ✅' if prediction[0]==1 else 'Died ❌'}")