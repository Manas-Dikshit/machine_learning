#matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. There is also a procedural "pylab" interface based on a state machine (like OpenGL), designed to closely resemble that of MATLAB, though its use is discouraged. SciPy makes use of Matplotlib.
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

print(matplotlib.__version__)

x = np.array([2023, 2024, 2025, 2026, 2027])
y1 = np.array([10, 35, 20, 25, 20])
y2 = np.array([16, 55, 20, 28, 19])
y3 = np.array([4, 5, 40, 65, 13])

# plt.plot(x, y1) #plotting the line graph
# plt.xlabel('Year') #labeling the x-axis
# plt.show() #displaying the graph


#labels
plt.title("Sample Plot", fontsize=25,
          family="Arial", fontweight="bold",
          color="red") #adding a title to the graph with custom font properties
plt.xlabel("Year", fontsize=20, color="green") #labeling the x-axis
plt.ylabel("Value", fontsize=20, color="green") #labeling the y-axis
plt.tick_params(axis='x', labelsize=15, color="blue") #customizing the x-axis tick parameters
plt.tick_params(axis='y', labelsize=15, color="blue") #customizing the y-axis tick parameters


#plot customization
plt.plot(x, y1, marker='o',
         markersize=10,
          markerfacecolor="#3115bd",
           markeredgecolor="cyan", linestyle='dotted',
            linewidth=2, color='#097d37') #customizing the line graph

line_style = dict(marker='o',
         markersize=10,
          markerfacecolor="#bdac15",
           markeredgecolor="blue", linestyle='solid',
            linewidth=2, color="#5B11A6")#customizing the line graph using a dictionary to store the style properties

plt.plot(x, y2, **line_style) #plotting the second line graph using the style properties from the dictionary
plt.plot(x, y3, **line_style) #plotting the third line graph using the style properties from the dictionary



plt.show() #displaying the graph


#grid() = helps to make plots easier to read by adding reference lines to the graph. It can be customized with various parameters to control the appearance of the grid lines, such as color, linestyle, and linewidth.

x2 = np.array([2023, 2024, 2025, 2026, 2027])
y4 = np.array([10, 35, 20, 25, 20])

plt.grid(color='gray', linestyle='--', linewidth=2.5) #adding a grid to the graph with custom properties

plt.plot(x2, y4, marker='o', markersize=10, markerfacecolor="#3115bd", markeredgecolor="cyan", linestyle='dotted', linewidth=2, color='#097d37')

plt.show()

#bar-Chart = a graphical representation of data using bars of different heights or lengths to represent the values of different categories. It is commonly used to compare the values of different categories or to show the distribution of data across categories.

categories = np.array(["Grains", "Vegetables", "Fruits", "Dairy", "Meat"])
values = np.array([30, 25, 20, 15, 10])

plt.bar(categories, values, color=['#5B11A6', '#097d37', '#bdac15', '#3115bd', 'cyan']) #creating a bar chart with custom colors for each bar


plt.title("Food Categories", fontsize=25, family="Arial", fontweight="bold", color="red") #adding a title to the bar chart with custom font properties
plt.xlabel("Categories", fontsize=20, color="green") #labeling the x-axis
plt.ylabel("Values", fontsize=20, color="green") #labeling the y-axis

plt.barh(categories, values, color=['#5B11A6', '#097d37', '#bdac15', '#3115bd', 'cyan']) #creating a horizontal bar chart with custom colors for each bar
plt.show() #displaying the bar chart



#Pie_chart = a circular statistical graphic, which is divided into slices to illustrate numerical proportion. In a pie chart, the arc length of each slice (and consequently its central angle and area) is proportional to the quantity it represents. While it is named for its resemblance to a pie which has been sliced, there are variations on the way it can be presented.

categories2 = np.array(["Freshman", "Sophomore", "Junior", "Senior"])
values2 = np.array([250, 320, 260, 285])
colors=['#5B11A6', '#097d37', '#bdac15', '#3115bd']

plt.pie(values2, labels=categories2, autopct='%1.1f%%', startangle=90, colors=colors, explode=[0, 0, 0, 0.1], shadow=True) #creating a pie chart with custom colors and displaying the percentage values for each slice
plt.title("Student Distribution by Year", fontsize=25, family="Arial", fontweight="bold", color="red") #adding a title to the pie chart with custom font properties
plt.axis('equal') #ensuring that the pie chart is circular
plt.show() #displaying the pie chart


#SCatter Graphs = a type of plot that displays the relationship between two variables by plotting individual data points on a Cartesian plane. Each point represents a pair of values, with one variable plotted on the x-axis and the other variable plotted on the y-axis. Scatter graphs are commonly used to visualize correlations, trends, and patterns in data.

xx = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
yy = np.array([25, 33, 57, 27, 81, 45, 60, 72, 90, 55])

xy = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
yx = np.array([45, 33, 77, 67, 41, 55, 40, 92, 90, 95])

plt.scatter(xx, yy, color='#5B11A6', marker='o', s=100, label="Class A") #creating a scatter graph with custom color, marker style, and size for the data points

plt.scatter(xy, yx, color='#097d37', marker='x', s=100, label="Class B") #creating a second scatter graph with custom color, marker style, and size for the data points

plt.title("Scatter Graph Example", fontsize=25, family="Arial", fontweight="bold", color="red") #adding a title to the scatter graph with custom font properties
plt.xlabel("X-axis", fontsize=20, color="green") #labeling the x-axis
plt.ylabel("Y-axis", fontsize=20, color="green") #labeling the y-axis
plt.grid(color='gray', linestyle='--', linewidth=0.5) #adding a grid to the scatter graph with custom properties
plt.legend()
plt.show() #displaying the scatter graph



#Histograms = a graphical representation of the distribution of numerical data. It is an estimate of the probability distribution of a continuous variable and was first introduced by Karl Pearson. To construct a histogram, the first step is to "bin" the range of values—that is, divide the entire range of values into a series of intervals—and then count how many values fall into each interval. The bins are usually specified as consecutive, non-overlapping intervals of a variable. The bins (intervals) must be adjacent, and are often (but not necessarily) of equal size. The histogram is then a plot of the number of values in each bin as bars.

scores = np.random.normal(loc=75, scale=10, size=1000) #generating random scores following a normal distribution with a mean of 75 and a standard deviation of 10
scores = np.clip(scores, 0, 100) #clipping the scores to be between 0 and 100 to represent valid score values

plt.hist(scores, bins=20, color="#11A620", edgecolor='black') #creating a histogram with custom number of bins, color, and edge color for the bars
plt.title("Distribution of Scores", fontsize=25, family="Arial", fontweight="bold", color="red") #adding a title to the histogram with custom font properties
plt.xlabel("Scores", fontsize=20, color="green") #labeling the x-axis
plt.ylabel("Frequency", fontsize=20, color="green") #labeling the y-axis
plt.grid(color='gray', linestyle='--', linewidth=0.5) #adding a grid to the histogram with custom properties
plt.show() #displaying the histogram


#Sub Plots = a feature in Matplotlib that allows you to create multiple plots within a single figure. This is useful for comparing different datasets or visualizing different aspects of the same dataset side by side. Subplots can be arranged in a grid format, and each subplot can have its own title, labels, and styling.
#Figure = the entire canvas
#Ax = A single Plot (SubPlot)

x = np.array([2023, 2024, 2025, 2026, 2027])
y1 = np.array([10, 35, 20, 25, 20])
y2 = np.array([16, 55, 20, 28, 19])

figure, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6)) #creating a figure with a grid of 1 row and 2 columns for subplots, and setting the figure size
axes[0].plot(x, y1, marker='o', markersize=10, markerfacecolor="#3115bd", markeredgecolor="cyan", linestyle='dotted', linewidth=2, color='#097d37') #plotting the first line graph on the first subplot
axes[0].set_title("Line Graph 1", fontsize=20, family="Arial", fontweight="bold", color="red") #adding a title to the first subplot with custom font properties
axes[0].set_xlabel("Year", fontsize=15, color="green") #labeling the x-axis of the first subplot
axes[0].set_ylabel("Value", fontsize=15, color="green") #labeling the y-axis of the first subplot
axes[0].grid(color='gray', linestyle='--', linewidth=0.5) #adding a grid to the first subplot with custom properties
axes[1].plot(x, y2, marker='o', markersize=10, markerfacecolor="#bdac15", markeredgecolor="blue", linestyle='solid', linewidth=2, color="#5B11A6") #plotting the second line graph on the second subplot
axes[1].set_title("Line Graph 2", fontsize=20, family="Arial", fontweight="bold", color="red") #adding a title to the second subplot with custom font properties
axes[1].set_xlabel("Year", fontsize=15, color="green") #labeling the x-axis of the second subplot
axes[1].set_ylabel("Value", fontsize=15, color="green") #labeling the y-axis of the second subplot
axes[1].grid(color='gray', linestyle='--', linewidth=0.5) #adding a grid to the second subplot with custom properties
plt.tight_layout() #adjusting the layout of the subplots to prevent overlap
plt.show() #displaying the figure with the subplots


#Pandas + MatplotLib


df = pd.read_csv("data.csv")

print(df.head())
print(df.columns)

plt.plot(df['number'], df['weight'],
         marker='o',
         markersize=10,
         markerfacecolor="#3115bd",
         markeredgecolor="cyan",
         linestyle='dotted',
         linewidth=2,
         color='#097d37')

plt.title("Pokemon Weight Chart",
          fontsize=25,
          family="Arial",
          fontweight="bold",
          color="red")

plt.xlabel("Pokemon Number", fontsize=20, color="green")
plt.ylabel("Weight", fontsize=20, color="green")

plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()