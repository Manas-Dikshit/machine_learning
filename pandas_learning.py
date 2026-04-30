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