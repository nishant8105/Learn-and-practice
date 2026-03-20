import pandas as pd

print("--- Pandas Data Manipulation ---\n")

# Create a sample DataFrame
data = {
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT'],
    'Employee': ['John', 'Jane', 'Mike', 'Susan', 'Tom', 'Emily'],
    'Salary': [75000, 65000, 80000, 90000, 60000, 78000],
    'Years_Experience': [3, 5, 2, 8, 4, 1]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n")

# 1. Filtering Data (Conditional Selection)
print("1. Filtering: Employees in 'IT' Department:")
it_employees = df[df['Department'] == 'IT']
print(it_employees)
print("\n")

print("2. Filtering: Salary greater than 75000:")
high_salary = df[df['Salary'] > 75000]
print(high_salary)
print("\n")

# 3. Grouping Data (Aggregation)
print("3. Grouping: Average Salary by Department:")
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
print(avg_salary_by_dept)
print("\n")

# 4. Sorting Data
print("4. Sorting: By Years of Experience (Descending):")
sorted_df = df.sort_values(by='Years_Experience', ascending=False)
print(sorted_df)
print("\n")

# 5. Adding a new column based on existing data
print("5. Adding a new column (Bonus = 10% of Salary):")
df['Bonus'] = df['Salary'] * 0.10
print(df)
print("\n")

# 6. Dealing with missing values (simulated)
import numpy as np
df.loc[2, 'Salary'] = np.nan # Introduce a missing value
print("6. DataFrame with a missing value in Salary:")
print(df)
print("\n")
print("Filling missing values with the mean salary:")
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df)
