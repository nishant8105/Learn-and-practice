import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from scipy.stats import pearsonr
from scipy.stats import chi2_contingency

df = pd.read_csv("insurance.csv")
print(df.head())

# EDA
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.histplot(x='age', data=df, kde=True)
plt.xlabel('Age')
plt.ylabel('Count')

plt.subplot(2, 2, 2)
sns.histplot(x='bmi', data=df, kde=True)
plt.xlabel('BMI')
plt.ylabel('Count')

plt.subplot(2, 2, 3)
sns.histplot(x='children', data=df, kde=True)
plt.xlabel('Children')
plt.ylabel('Count')

plt.subplot(2, 2, 4)
sns.histplot(x='charges', data=df, kde=True)
plt.xlabel('Charges')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

# Data Cleaning and preprocessing
df_clean = df.copy()
# print(df.shape)
df_clean.drop_duplicates(inplace=True)
print(df.shape)
print(df_clean.isnull().sum())
print(df_clean['sex'].value_counts())
df_clean['sex'] = df_clean['sex'].map({"male" : 0, "female" : 1})
df_clean['smoker'] =  df_clean['smoker'].map({"no" : 0, "yes" : 1})
df_clean = pd.get_dummies(df_clean, columns=["region"], drop_first=True)
df_clean.rename(columns={
    "sex" :"is_female",
    "smoker" : "is_smoker"
}, inplace=True)

df_clean = df_clean.astype(int)
# print(df_clean.head())

# feature Engineering
df_clean['bmi_category'] = pd.cut(
    df_clean['bmi'],
    bins=[0, 18, 24.9, 29.9, float('inf')],
    labels=['Underweight', 'Normal', 'Overweight', 'Obese']
)
df_clean = pd.get_dummies(df_clean, columns=["bmi_category"], drop_first=True)
df_clean = df_clean.astype(int)
print(df_clean.head())
cols = ['age', 'bmi','children' ]
scaler = StandardScaler()
df_clean[cols] = scaler.fit_transform(df_clean[cols])
print(df_clean.head())

# fearture Extraction

selected_features = ['age', 'is_female', 'bmi', 'children', 'is_smoker',
       'region_northwest', 'region_southeast', 'region_southwest',
       'bmi_category_Normal', 'bmi_category_Overweight', 'bmi_category_Obese']

correlations = {
    feature : pearsonr(df_clean[feature], df_clean['charges'])[0]
    for feature in selected_features
}
correlations_df = pd.DataFrame(list(correlations.items()), columns=['Fearute','Pearson Correlation'])
correlations_df.sort_values(by="Pearson Correlation", ascending=False, inplace=True)
print(correlations_df)

cat_feature = ['is_female','is_smoker',
       'region_northwest', 'region_southeast', 'region_southwest',
       'bmi_category_Normal', 'bmi_category_Overweight', 'bmi_category_Obese']

alpha = 0.05
df_clean['charges_bin'] = pd.qcut(df_clean['charges'], q=4, labels=False)
chi2_result = {}

for col in cat_feature:
    contingency = pd.crosstab(df_clean[col], df_clean['charges_bin'])
    chi2_stat, p_val , _ , _ = chi2_contingency(contingency)
    decision = 'Reject Null (Keep Feature)' if p_val < alpha else "Accept Null (Drop Feature)"
    chi2_result[col] = {
        'Chi2_Statistic' : chi2_stat,
        'p_value' : p_val,
        'Decision' : decision
    }

chi2_df = pd.DataFrame(chi2_result).T
chi2_df = chi2_df.sort_values(by="p_value")
print(chi2_df)

final_df = df_clean[['age', 'is_female', 'bmi', 'children', 'is_smoker', 'charges','region_southeast' , 'bmi_category_Obese']]
print(final_df.head())