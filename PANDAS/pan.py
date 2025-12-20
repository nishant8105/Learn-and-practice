# Import the necessary libraries
import pandas as pd
import seaborn as sns

# TODO: Load the Titanic dataset into a pandas DataFrame
df = sns.load_dataset('titanic')
# TODO: Output the first 5 rows of the DataFrame
print("First 5 rows of the original DataFrames")
print(df.head())
# TODO: Create a new column, "IsChild", to identify the passengers who are under 18
df["IsChild"] = df["age"]<18
# TODO: Output the DataFrame after the addition of the 'IsChild' column
print(df.head())