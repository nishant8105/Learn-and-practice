import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV,
    train_test_split,
    StratifiedKFold
)
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (
    RobustScaler, OneHotEncoder
)
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score

# ── Load Data ────────────────────────────────────────
url = "git_titanic.csv"
df  = pd.read_csv(url)
df.drop(['PassengerId','Name','Ticket','Cabin'],
        axis=1, inplace=True)

X = df.drop('Survived', axis=1)
y = df['Survived']

# ── Column Setup ─────────────────────────────────────
numeric_cols     = ['Age','Fare','SibSp','Parch']
categorical_cols = ['Sex','Embarked','Pclass']

# ── Preprocessor ─────────────────────────────────────
num_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler',  RobustScaler())
])
cat_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore',
                              sparse_output=False))
])
preprocessor = ColumnTransformer([
    ('num', num_pipe, numeric_cols),
    ('cat', cat_pipe, categorical_cols)
])

# ── Split ─────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
# ── GridSearchCV ─────────────────────────────────────
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestClassifier(random_state=42))
])

# Define grid
param_grid = {
    'model__n_estimators' : [50, 100, 200],
    'model__max_depth'    : [3, 5, 10, None],
    'model__min_samples_split': [2, 5, 10],
}
# Note: 'model__' prefix because param is inside pipeline

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

grid_search = GridSearchCV(
    pipeline,
    param_grid,
    cv=cv,
    scoring='accuracy',
    n_jobs=-1,        # Use all CPU cores
    verbose=1         # Show progress
)

grid_search.fit(X_train, y_train)

# ── Results ───────────────────────────────────────────
print("=" * 45)
print(f"  Best CV Score : {grid_search.best_score_:.4f}")
print(f"  Best Params   :")
for k, v in grid_search.best_params_.items():
    print(f"    {k:<35} {v}")
print("=" * 45)

# Test score with best model
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
print(f"\n  Test Accuracy : {accuracy_score(y_test, y_pred):.4f}")
