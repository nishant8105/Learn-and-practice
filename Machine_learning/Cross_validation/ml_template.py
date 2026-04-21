# ════════════════════════════════════════════════════
#   COMPLETE ML PROJECT TEMPLATE
#   EDA → Pipeline → Tuning → Evaluate → Save
# ════════════════════════════════════════════════════

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import optuna
optuna.logging.set_verbosity(optuna.logging.WARNING)

from sklearn.model_selection import (
    train_test_split, StratifiedKFold,
    cross_val_score
)
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, classification_report,
    confusion_matrix, ConfusionMatrixDisplay
)

# ── STEP 1: LOAD ─────────────────────────────────────
print("📦 STEP 1: Loading data...")
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df  = pd.read_csv(url)
df.drop(['PassengerId','Name','Ticket','Cabin'],
        axis=1, inplace=True)
print(f"   Shape: {df.shape}")

# ── STEP 2: QUICK EDA ────────────────────────────────
print("\n🔍 STEP 2: Quick EDA...")
print(f"   Missing:\n{df.isnull().sum()[df.isnull().sum()>0]}")
print(f"   Target balance:\n{df['Survived'].value_counts()}")

# ── STEP 3: PREPARE ──────────────────────────────────
print("\n⚙️  STEP 3: Preparing features...")
X = df.drop('Survived', axis=1)
y = df['Survived']

numeric_cols     = ['Age','Fare','SibSp','Parch']
categorical_cols = ['Sex','Embarked','Pclass']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"   Train: {X_train.shape}, Test: {X_test.shape}")

# ── STEP 4: BUILD PIPELINE ───────────────────────────
print("\n🔧 STEP 4: Building pipeline...")
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

# ── STEP 5: TUNE WITH OPTUNA ─────────────────────────
print("\n🎯 STEP 5: Tuning hyperparameters...")

def objective(trial):
    params = {
        'n_estimators'     : trial.suggest_int('n_estimators', 50, 300),
        'max_depth'        : trial.suggest_int('max_depth', 3, 15),
        'min_samples_split': trial.suggest_int('min_samples_split', 2, 10),
        'min_samples_leaf' : trial.suggest_int('min_samples_leaf', 1, 5),
        'max_features'     : trial.suggest_categorical(
                                'max_features', ['sqrt','log2'])
    }
    pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('model', RandomForestClassifier(**params, random_state=42))
    ])
    return cross_val_score(
        pipe, X_train, y_train,
        cv=5, scoring='accuracy', n_jobs=-1
    ).mean()

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=50, show_progress_bar=True)
print(f"   Best CV Score: {study.best_value:.4f}")

# ── STEP 6: TRAIN FINAL MODEL ────────────────────────
print("\n🏋️  STEP 6: Training final model...")
final_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestClassifier(
        **study.best_params, random_state=42))
])
final_pipeline.fit(X_train, y_train)

# ── STEP 7: EVALUATE ─────────────────────────────────
print("\n📊 STEP 7: Evaluating...")
y_pred = final_pipeline.predict(X_test)

print(f"\n{'='*45}")
print(f"  Test Accuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"{'='*45}")
print(classification_report(y_test, y_pred,
      target_names=['Died','Survived']))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=['Died','Survived']
)
disp.plot(cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

# ── STEP 8: SAVE ─────────────────────────────────────
print("\n💾 STEP 8: Saving...")
joblib.dump(final_pipeline, 'final_model.pkl')
print("   ✅ Saved to final_model.pkl")

print("\n🎉 PROJECT COMPLETE!")