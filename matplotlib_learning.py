#matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. There is also a procedural "pylab" interface based on a state machine (like OpenGL), designed to closely resemble that of MATLAB, though its use is discouraged. SciPy makes use of Matplotlib.
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# print(matplotlib.__version__)

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


