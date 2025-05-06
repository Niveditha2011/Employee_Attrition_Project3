import pandas as pd

# Load raw data
df = pd.read_csv('data/raw_data.csv')

# --- Binary Encoding ---
binary_map = {
    'Attrition': lambda x: 1 if str(x).strip().lower() == 'yes' else 0,
    'Gender': lambda x: 1 if str(x).strip().lower() == 'male' else 0,
    'Over18': lambda x: 1 if str(x).strip().lower() == 'y' else 0,
    'OverTime': lambda x: 1 if str(x).strip().lower() == 'yes' else 0
}

for col, func in binary_map.items():
    df[col] = df[col].apply(func)

# --- One-Hot Encoding ---
df = df.join(pd.get_dummies(df['BusinessTravel'], prefix='BusinessTravel')).drop('BusinessTravel', axis=1)
df = df.join(pd.get_dummies(df['Department'], prefix='Department')).drop('Department', axis=1)
df = df.join(pd.get_dummies(df['EducationField'], prefix='Education')).drop('EducationField', axis=1)
df = df.join(pd.get_dummies(df['JobRole'], prefix='Role')).drop('JobRole', axis=1)
df = df.join(pd.get_dummies(df['MaritalStatus'], prefix='MaritalStatus')).drop('MaritalStatus', axis=1)

# --- Drop Irrelevant or Constant Columns ---
df = df.drop(['EmployeeNumber', 'EmployeeCount', 'Over18', 'StandardHours'], axis=1)

# --- Convert True/False to 1/0 if any ---
df = df.map(lambda x: 1 if x is True else 0 if x is False else x)

# Save cleaned data
df.to_csv('data/cleaned_employee_data.csv', index=False)
print("Data preprocessing complete. Cleaned data saved to 'data/cleaned_employee_data.csv'")
