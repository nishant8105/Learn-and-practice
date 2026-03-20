import pandas as pd

print("--- Pandas Basics: Creating and Viewing Data ---\n")

# 1. Creating a Series (1D array)
print("1. Creating a Series:")
data_series = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(data_series)
print("\n")

# 2. Creating a DataFrame (2D table) from a dictionary
print("2. Creating a DataFrame:")
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 28, 22],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Score': [85, 92, 78, 88, 95]
}
df = pd.DataFrame(data_dict)
print(df)
print("\n")

# 3. Viewing the top rows (useful for large datasets)
print("3. Viewing the first 2 rows using head():")
print(df.head(2))
print("\n")

# 4. Accessing a specific column
print("4. Accessing the 'Name' column:")
print(df['Name'])
print("\n")

# 5. Accessing a specific row by index using iloc (integer location)
print("5. Accessing the 3rd row (index 2) using iloc:")
print(df.iloc[2])
print("\n")

# 6. Basic statistics
print("6. Getting basic statistics using describe():")
print(df.describe())
