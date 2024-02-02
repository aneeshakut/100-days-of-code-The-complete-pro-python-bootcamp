import pandas as pd

# Creating a Series
s = pd.Series([1, 3, 5, None, 6, 8])

# Creating a DataFrame
df = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco']
})

# Accessing columns in DataFrame
name_column = df['Name']
age_column = df['Age']
city_column = df['City']

# Adding a new column to DataFrame
df['Gender'] = ['Male', 'Female', 'Male', 'Male']

# Filtering rows based on a condition
young_people = df[df['Age'] < 30]

# Creating CSV data within the program using a list of dictionaries
csv_data = [
    {'ID': 1, 'Product': 'Apple', 'Price': 1.00},
    {'ID': 2, 'Product': 'Banana', 'Price': 0.75},
    {'ID': 3, 'Product': 'Orange', 'Price': 1.25},
    {'ID': 4, 'Product': 'Grapes', 'Price': 2.00}
]

# Reading data from a list of dictionaries into a DataFrame
csv_df = pd.DataFrame(csv_data)

# Displaying the Series and DataFrame
print("Series:")
print(s)

print("\nDataFrame:")
print(df)

print("\nName Column:")
print(name_column)

print("\nAge Column:")
print(age_column)

print("\nCity Column:")
print(city_column)

print("\nDataFrame with Gender Column:")
print(df)

print("\nYoung People:")
print(young_people)

print("\nData from CSV:")
print(csv_df)
