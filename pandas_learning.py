#Pandas is a python library used in data analysis, data science, machine learning.
# series = 1D array
# DataFrame = 2D array
# Pandas is built on top of NumPy and provides additional functionality for data manipulation and analysis.
#We can import, display, and manipulate data using pandas.

import pandas as pd

print(pd.__version__) #to print pandas version

#Series
# A Series is a one-dimensional labeled array that can hold any data type (integers, strings, floating-point numbers, etc.).
# Each element in a Series is associated with an index, which can be used to access and manipulate the data.

data = [10, 20, 30, 40, 50]
float_checking = [1.5, 2.5, 3.5, 4.5, 5.5]
object_checking = ['A', 'B', 'C', 'D', 'E']
boolean_checking = [True, False, True, False, True]
series = pd.Series(data)
series_float = pd.Series(float_checking)
series_object = pd.Series(object_checking)
series_boolean = pd.Series(boolean_checking)
print(series)
print(series_float)
print(series_object)
print(series_boolean)

#custom labels
series_labels = pd.Series(data, index = ['a', 'b', 'c', 'd', 'e'])
print(series_labels)
series_labels.loc["c"] = 100 #modifying element using custom label
print(series_labels.loc["a"]) #accessing element using custom label
print(series_labels.loc["c"]) #accessing element using custom label
print(series_labels.iloc[0]) #accessing element using integer position
print(series_labels.iloc[2]) #accessing element using integer position

print(series[series > 25]) #filtering elements greater than 25

calories = {"day1": 1200, "day2": 2250, "day3": 2300}
calories_series = pd.Series(calories)
calories_series.loc["day2"] += 2000 #modifying element using custom label
print(calories_series)
print(calories_series[calories_series > 2000]) #filtering elements greater than 2000


#DataFrame
# A DataFrame is a two-dimensional labeled data structure that can hold data of different types (like a spreadsheet or SQL table).
# It consists of rows and columns, where each column can be of a different data type (e.g., integers, floats, strings).
# DataFrames are widely used for data manipulation, analysis, and visualization.
#A tabular data structure that organizes data into rows and columns, similar to a spreadsheet or SQL table. Each column can contain different types of data (e.g., integers, floats, strings), and each row represents a record or observation.
#DataFrames are built on top of Series, where each column in a DataFrame is essentially a Series.

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],"Age": [25, 30, 35, 40],}
df = pd.DataFrame(data)
df_labels = pd.DataFrame(data, index = ['a', 'b', 'c', 'd'])
print(df)
print(df_labels)
print(df_labels.loc["a"]) #accessing row using custom label
print(df.iloc[0]) #accessing row using integer position
print(df_labels["Name"]) #accessing column using column name
print(df_labels["Age"]) #accessing column using column name

# Add a new Coloumn
df_labels["City"] = ["New York", "Los Angeles", "Chicago", "Houston"] #adding new column to DataFrame
print(df_labels)

# Add a new Row
new_row = pd.DataFrame([{"Name": "Eve", "Age": 28, "City": "Phoenix"}], index=["e"]) #creating new row as a DataFrame
df_labels = pd.concat([df_labels, new_row], ignore_index=True) #adding new row to DataFrame
print(df_labels)


#importing csv and excel files
# We can use the read_csv() function to read a CSV file and the read_excel() function to read an Excel file. These functions return a DataFrame that contains the data from the file.

df_csv = pd.read_csv("data.csv") #reading csv file
print(df_csv)
print(df_csv.to_string()) #to print entire DataFrame without truncation

#importing json files
df_json = pd.read_json("data.json") #reading json file
print(df_json)