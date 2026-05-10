#matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. There is also a procedural "pylab" interface based on a state machine (like OpenGL), designed to closely resemble that of MATLAB, though its use is discouraged. SciPy makes use of Matplotlib.
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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