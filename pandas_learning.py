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


#Selection and Filtering
# We can select specific columns from a DataFrame using the column names. We can also filter rows based on certain conditions using boolean indexing.

# SELECTION BY COLOUMN
print(df_csv["name"]) #selecting a column by name
print(df_csv[["name", "height"]]) #selecting multiple columns by name
print(df_csv["name"].to_string()) #to print entire column without truncation

#SELECTION BY ROWS
print(df_csv.loc[0]) #selecting a row by index label
print(df_csv.iloc[0]) #selecting a row by integer position

df_csv_updated = pd.read_csv("data.csv", index_col="name") #reading csv file with name column as index
print(df_csv_updated) 
print(df_csv_updated.loc["Raichu"]) #selecting a row by index label
print(df_csv_updated.loc["Raichu"]["height"]) #selecting a specific value by row and column labels
print(df_csv_updated.loc["Raichu" : "Mewtwo"]["height"]) #selecting a specific value by row and column labels
print(df_csv.iloc[0:5]) #selecting multiple rows by integer position

#USER INPUT AND FINDING IT IN CSV FILE
pokemon = input("Enter the name of a Pokemon: ")

try:
    print(df_csv_updated.loc[pokemon]) #selecting a row by index label
except KeyError:
    print(f"{pokemon} not found in the DataFrame.")



#Filetering = Keeping the rows that match a condition

tall_pokemon = df_csv[df_csv["height"] >= 2.0] #filtering rows based on a height condition
print(tall_pokemon)

heavy_pokemon = df_csv[df_csv["weight"] >= 100.0] #filtering rows based on a weight condition
print(heavy_pokemon)

legendary_pokemon = df_csv[df_csv["legendary"] == True] #filtering rows based on a boolean condition
print(legendary_pokemon)

water_pokemon = df_csv[df_csv["type1"] == "Water"] #filtering rows based on a string condition

water_pokemon_two_types = df_csv[(df_csv["type1"] == "Water") | (df_csv["type2"] == "Water")] #filtering rows based on multiple string conditions
print(water_pokemon_two_types)
print(water_pokemon)

fire_flying_pokemon = df_csv[(df_csv["type1"] == "Fire") & (df_csv["type2"] == "Flying")] #filtering rows based on multiple string conditions
print(fire_flying_pokemon)


# Aggregate Functions
# We can use aggregate functions to perform calculations on the data in a DataFrame. Some common aggregate functions include mean(), sum(), count(), min(), and max().
# There functions reduces a set of values into a single summary value used to summerize and analyze data often used the groupby() function to group data by a specific column and then apply an aggregate function to each group.

df_for_aggregate = pd.read_csv("data.csv") #reading csv file


print(df_for_aggregate.mean(numeric_only=True))
print(df_for_aggregate["height"].mean()) #calculating mean of a specific column
print(df_for_aggregate["weight"].mean()) #calculating mean of a specific column
print(df_for_aggregate.sum(numeric_only=True)) #calculating sum of all numeric columns
print(df_for_aggregate["height"].sum()) #calculating sum of a specific 
print(df_for_aggregate.min(numeric_only=True))#calculating minimum value of all numeric columns
print(df_for_aggregate["height"].min()) #calculating minimum value of a specific column
print(df_for_aggregate.max(numeric_only=True)) #calculating maximum value of all numeric columns
print(df_for_aggregate["height"].max()) #calculating maximum value of a specific column

group = df_for_aggregate.groupby("type1") #grouping data by type1 column
print(group["height"].mean()) #calculating mean of each group
print(group["height"].sum()) #calculating sum of each group
print(group["height"].min()) #calculating minimum value of each group