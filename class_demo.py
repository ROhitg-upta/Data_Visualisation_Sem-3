import pandas as pd

# 1. Working with Series (1D Data)
marks = pd.Series([80, 90, 95, 88])
print("--- Pandas Series ---")
print(marks)
print()

# 2. Creating a DataFrame from Dictionary
data = {
    "Name": ["Vikky", "Rahul", "Aman"],
    "Age": [22, 21, 32],
    "Marks": [89, 98, 76]
}
df_dict = pd.DataFrame(data)
print("--- DataFrame from Dictionary ---")
print(df_dict)
print()

# 3. Reading from CSV (xyz.csv)
df = pd.read_csv("xyz.csv")
print("--- DataFrame from xyz.csv ---")
print(df.head())
print()

# 4. DataFrame Inspection Methods
print("--- Head (First 5 rows) ---")
print(df.head())

print("\n--- Tail (Last 5 rows) ---")
print(df.tail())

print("\n--- Shape (Rows, Columns) ---")
print(df.shape)

print("\n--- DataFrame Info ---")
df.info()

print("\n--- Column Names ---")
print(df.columns)

print("\n--- Statistical Summary ---")
print(df.describe())
