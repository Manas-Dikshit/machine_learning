Seaborn for Machine Learning — Complete Notes (Basic → Advanced)

1. Introduction to Seaborn

Seaborn is a high-level Python data visualization library built on top of:

- matplotlib
- pandas
- numpy

It provides:

- Beautiful statistical graphics
- Better default styles
- Simpler syntax
- Powerful integration with DataFrames

It is heavily used in:

- Exploratory Data Analysis (EDA)
- Machine Learning workflows
- Statistical analysis
- Feature analysis
- Model diagnostics

2. Installation
```bash
pip install seaborn
```

3. Importing Libraries
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```

4. Loading Built-in Datasets
```python
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
flights = sns.load_dataset("flights")
diamonds = sns.load_dataset("diamonds")

# View dataset:
print(tips.head())
```

5. Seaborn Themes & Styles

Set Theme
```python
sns.set_theme()
```
Styles
```python
sns.set_style("darkgrid")
sns.set_style("whitegrid")
sns.set_style("ticks")
sns.set_style("white")
sns.set_style("dark")
```
Context

Controls scaling of labels.
```python
sns.set_context("paper")
sns.set_context("notebook")
sns.set_context("talk")
sns.set_context("poster")
```

6. Distribution Plots

Used to understand data distribution.

6.1 Histogram (histplot)
```python
sns.histplot(data=tips, x="total_bill")
plt.show()
```
With KDE
```python
sns.histplot(data=tips, x="total_bill", kde=True)
```
Multiple Categories
```python
sns.histplot(data=tips, x="total_bill", hue="sex")
```

6.2 KDE Plot (kdeplot)

Kernel Density Estimation.
```python
sns.kdeplot(data=tips, x="total_bill")
```
Filled KDE
```python
sns.kdeplot(data=tips, x="total_bill", fill=True)
```
Bivariate KDE
```python
sns.kdeplot(data=tips, x="total_bill", y="tip")
```

6.3 Rug Plot
```python
sns.rugplot(data=tips, x="total_bill")
```

6.4 ECDF Plot

Empirical cumulative distribution function.
```python
sns.ecdfplot(data=tips, x="total_bill")
```

7. Categorical Plots
7.1 Count Plot

Frequency counts.
```python
sns.countplot(data=tips, x="day")
```
Horizontal
```python
sns.countplot(data=tips, y="day")
```
7.2 Bar Plot

Shows mean values.
```python
sns.barplot(data=tips, x="day", y="total_bill")
```
With Hue
```python
sns.barplot(data=tips, x="day", y="total_bill", hue="sex")
```
7.3 Box Plot

Excellent for outlier detection.
```python
sns.boxplot(data=tips, x="day", y="total_bill")
```
With Hue
```python
sns.boxplot(data=tips, x="day", y="total_bill", hue="smoker")
```
7.4 Violin Plot

Combines boxplot + KDE.
```python
sns.violinplot(data=tips, x="day", y="total_bill")
```
Split Violin
```python
sns.violinplot(data=tips,
               x="day",
               y="total_bill",
               hue="sex",
               split=True)
```
7.5 Strip Plot
```python
sns.stripplot(data=tips, x="day", y="total_bill")
```
With Jitter
```python
sns.stripplot(data=tips,
              x="day",
              y="total_bill",
              jitter=True)
```
7.6 Swarm Plot

Avoids overlap.
```python
sns.swarmplot(data=tips, x="day", y="total_bill")
```

8. Relational Plots
8.1 Scatter Plot
```python
sns.scatterplot(data=tips,
                x="total_bill",
                y="tip")
```
Hue & Size
```python
sns.scatterplot(data=tips,
                x="total_bill",
                y="tip",
                hue="sex",
                size="size")
```
8.2 Line Plot
```python
sns.lineplot(data=flights,
             x="year",
             y="passengers")
```

9. Regression Plots

Very important in ML.

9.1 Regression Plot
```python
sns.regplot(data=tips,
            x="total_bill",
            y="tip")
```
Polynomial Regression
```python
sns.regplot(data=tips,
            x="total_bill",
            y="tip",
            order=2)
```
9.2 Linear Model Plot
```python
sns.lmplot(data=tips,
           x="total_bill",
           y="tip",
           hue="sex")
```

10. Matrix Plots
10.1 Heatmap

Most important plot in ML.

Correlation Matrix
```python
corr = tips.corr(numeric_only=True)

sns.heatmap(corr)
```
Annotated Heatmap
```python
sns.heatmap(corr,
            annot=True,
            cmap="coolwarm")
```
Important Parameters
Parameter	Description
annot	Show values
cmap	Color map
linewidths	Cell borders
fmt	Number formatting
cbar	Color bar
10.2 Clustermap

Hierarchical clustering.
```python
sns.clustermap(corr)
```

11. Pair Plot

Extremely useful in EDA.
```python
sns.pairplot(iris)
```
With Hue
```python
sns.pairplot(iris, hue="species")
```
KDE Diagonal
```python
sns.pairplot(iris,
             hue="species",
             diag_kind="kde")
```

12. Joint Plot

Combines scatter + histogram/KDE.
```python
sns.jointplot(data=tips,
              x="total_bill",
              y="tip")
```
KDE Jointplot
```python
sns.jointplot(data=tips,
              x="total_bill",
              y="tip",
              kind="kde")
```
Hex Plot
```python
sns.jointplot(data=tips,
              x="total_bill",
              y="tip",
              kind="hex")
```

13. Facet Grid

Create subplots based on categories.
```python
g = sns.FacetGrid(tips, col="time")
g.map(sns.scatterplot, "total_bill", "tip")
```

14. Pair Grid

Advanced customizable pairplot.
```python
g = sns.PairGrid(iris)
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
```

15. Catplot

Figure-level categorical plot.
```python
sns.catplot(data=tips,
            x="day",
            y="total_bill",
            kind="box")
```
Types
strip
swarm
box
violin
boxen
point
bar
count

16. Relplot

Figure-level relational plot.
```python
sns.relplot(data=tips,
            x="total_bill",
            y="tip",
            hue="sex")
```

17. Displot

Figure-level distribution plot.
```python
sns.displot(data=tips,
            x="total_bill",
            kde=True)
```

18. Working with Colors
Color Palettes
```python
sns.color_palette()
```
Built-in Palettes
```python
sns.color_palette("deep")
sns.color_palette("muted")
sns.color_palette("pastel")
sns.color_palette("bright")
sns.color_palette("dark")
sns.color_palette("colorblind")
```
Set Palette
```python
sns.set_palette("deep")
```

19. Customization
Figure Size
```python
plt.figure(figsize=(10,5))
```
Title & Labels
```python
plt.title("Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Revenue")
```
Rotation
```python
plt.xticks(rotation=45)
```
Save Figure
```python
plt.savefig("plot.png")
```

20. Machine Learning EDA Workflow with Seaborn
Step 1: Understand Data
```python
df.info()
df.describe()
df.isnull().sum()
```
Step 2: Univariate Analysis
```python
sns.histplot(df["Age"], kde=True)
```

Goal:

Detect skewness
Detect outliers
Understand distribution
Step 3: Bivariate Analysis
```python
sns.scatterplot(data=df,
                x="Age",
                y="Salary")
```

Goal:

Correlation
Trends
Clusters
Step 4: Correlation Analysis
```python
sns.heatmap(df.corr(numeric_only=True),
            annot=True)
```

Goal:

Feature selection
Remove multicollinearity
Step 5: Outlier Detection
```python
sns.boxplot(data=df, y="Salary")
```
Step 6: Class Imbalance
```python
sns.countplot(data=df, x="target")
```

21. Seaborn in Classification Problems
Visualize Decision Boundaries
```python
sns.scatterplot(data=df,
                x="feature1",
                y="feature2",
                hue="target")
```
Confusion Matrix Heatmap
```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_true, y_pred)

sns.heatmap(cm,
            annot=True,
            fmt="d")
```

22. Seaborn in Regression Problems
Regression Relationship
```python
sns.regplot(data=df,
            x="experience",
            y="salary")
```
Residual Analysis
```python
sns.residplot(data=df,
              x="experience",
              y="salary")
```

23. Time Series Visualization
```python
sns.lineplot(data=df,
             x="date",
             y="sales")
```
Multiple Categories
```python
sns.lineplot(data=df,
             x="date",
             y="sales",
             hue="region")
```

24. Advanced Seaborn Concepts
24.1 Figure-Level vs Axes-Level Functions
Axes-Level

Returns matplotlib axes.

Examples:

scatterplot
histplot
boxplot
sns.scatterplot(...)
Figure-Level

Creates entire figure.

Examples:

relplot
displot
catplot
lmplot
sns.relplot(...)

24.2 Statistical Estimation

Seaborn automatically computes:

- Mean
- Confidence intervals
- Regression fit

Example:
```python
sns.barplot(data=tips,
            x="day",
            y="total_bill")
```

24.3 Confidence Intervals
```python
sns.lineplot(data=df,
             x="x",
             y="y",
             errorbar="sd")
```

24.4 Handling Missing Data

Seaborn automatically ignores NaN values.
```python
sns.histplot(df["age"])
```

24.5 Semantic Mapping

Seaborn supports:

Semantic	Meaning
hue	Color grouping
size	Size grouping
style	Marker styles

Example:
```python
sns.scatterplot(data=tips,
                x="total_bill",
                y="tip",
                hue="sex",
                size="size",
                style="smoker")
```

25. Performance Tips
- Use Sampling for Huge Datasets
```python
sample_df = df.sample(10000)
```
- Avoid Pairplot on Large Data

Pairplots become very slow.

- Use Alpha for Dense Data
```python
sns.scatterplot(data=df,
                x="x",
                y="y",
                alpha=0.3)
```

26. Common Interview Questions
Q1: Difference between Matplotlib and Seaborn?
Matplotlib	Seaborn
Low-level	High-level
More control	Easier syntax
Less beautiful defaults	Better aesthetics
General plotting	Statistical visualization
Q2: Difference between countplot and barplot?
Countplot

Counts frequency.

sns.countplot(x="day")
Barplot

Shows aggregated values (mean by default).

sns.barplot(x="day", y="sales")
Q3: Difference between stripplot and swarmplot?
Stripplot	Swarmplot
Can overlap	Avoids overlap
Faster	Slower
Q4: Why use Heatmaps?
Correlation analysis
Feature selection
Detect multicollinearity

27. Best Plots for Machine Learning
Task	Recommended Plot
Distribution	histplot, kdeplot
Correlation	heatmap
Outliers	boxplot
Relationships	scatterplot
Regression	regplot
Feature interactions	pairplot
Class balance	countplot
Time series	lineplot

28. Real ML Example
```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

# Missing values
print(df.isnull().sum())

# Survival count
sns.countplot(data=df, x="survived")

# Age distribution
sns.histplot(data=df, x="age", kde=True)

# Correlation heatmap
corr = df.corr(numeric_only=True)

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.show()
```

29. Seaborn Cheat Sheet
Plot	Function
Histogram	histplot
KDE	kdeplot
Scatter	scatterplot
Line	lineplot
Box	boxplot
Violin	violinplot
Count	countplot
Heatmap	heatmap
Pairplot	pairplot
Regression	regplot
Jointplot	jointplot
Catplot	catplot
Relplot	relplot


---

## Introduction

Seaborn is a high-level Python visualization library built on top of Matplotlib, Pandas, and NumPy. It provides beautiful default styles and concise APIs tailored for statistical graphics and EDA.

## Installation

Install via pip:

```bash
pip install seaborn
```

## Quick Start

Import essentials:

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# load example dataset
tips = sns.load_dataset('tips')
```

Show a simple plot:

```python
sns.histplot(data=tips, x='total_bill', kde=True)
plt.show()
```

## Core Plot Types

### Distribution Plots

- histplot: histograms with optional KDE
- kdeplot: kernel density estimates
- ecdfplot: empirical CDF

Example:

```python
sns.histplot(tips, x='total_bill', kde=True)
sns.kdeplot(tips['tip'], fill=True)
sns.ecdfplot(tips, x='total_bill')
```

### Categorical Plots

- countplot: frequency counts
- barplot: aggregated values (mean by default)
- boxplot / violinplot: outliers & distribution shapes
- stripplot / swarmplot: individual points

Example:

```python
sns.countplot(data=tips, x='day')
sns.barplot(data=tips, x='day', y='total_bill', hue='sex')
sns.boxplot(data=tips, x='day', y='total_bill')
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True)
```

### Relational Plots

- scatterplot: scatter with semantic mappings (hue/size/style)
- lineplot: trends over continuous x (time series)

Example:

```python
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', size='size')
flights = sns.load_dataset('flights').pivot('month', 'year', 'passengers')
sns.lineplot(data=sns.load_dataset('flights'), x='year', y='passengers')
```

### Regression & Model Diagnostics

- regplot: scatter + regression line (order for polynomial)
- lmplot: figure-level linear model with facets/hue
- residplot: residual analysis

Example:

```python
sns.regplot(data=tips, x='total_bill', y='tip', order=1)
sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex')
sns.residplot(data=tips, x='total_bill', y='tip')
```

### Matrix & Pair Plots

- heatmap: correlation matrices or 2D grids
- clustermap: heatmap with hierarchical clustering
- pairplot / PairGrid: pairwise relationships

Example:

```python
corr = tips.corr(numeric_only=True)
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
sns.pairplot(sns.load_dataset('iris'), hue='species')
```

### Facets & Grids

- FacetGrid: custom small multiples
- catplot / relplot / displot: figure-level plots with easy faceting

Example:

```python
g = sns.FacetGrid(tips, col='time')
g.map(sns.scatterplot, 'total_bill', 'tip')

# catplot example
sns.catplot(data=tips, x='day', y='total_bill', kind='box')
```

## Customization & Styles

Seaborn provides theme and palette helpers:

```python
sns.set_theme(style='whitegrid')
sns.set_context('notebook')
sns.set_palette('deep')
plt.figure(figsize=(10,6))
```

Color palettes: `deep`, `muted`, `pastel`, `bright`, `dark`, `colorblind`.

Figure-level vs Axes-level: figure-level functions (e.g., `relplot`, `catplot`, `displot`) create a full figure and manage faceting; axes-level functions (e.g., `scatterplot`, `histplot`) return an `Axes` you can further customize.

## Machine Learning Usage

Suggested EDA workflow:

1. Data overview: `df.info()`, `df.describe()`, `df.isnull().sum()`
2. Univariate analysis: `histplot`, `kdeplot`, `boxplot`
3. Bivariate analysis: `scatterplot`, `regplot`, `heatmap` for correlation
4. Outlier detection: `boxplot` / `violinplot`
5. Class balance: `countplot`

Example: confusion matrix visualization

```python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
```

## Performance Tips

- Sample large datasets: `df.sample(n)`
- Use `alpha` for dense scatterplots to reduce overplotting
- Avoid `pairplot` on very large datasets
- Use vectorized Pandas operations before plotting (reduce Python loops)

## Cheat Sheet

Plot → Function

- Histogram → `histplot`
- KDE → `kdeplot`
- Scatter → `scatterplot`
- Line → `lineplot`
- Box → `boxplot`
- Violin → `violinplot`
- Count → `countplot`
- Heatmap → `heatmap`
- Pairplot → `pairplot`
- Regression → `regplot` / `lmplot`
- Jointplot → `jointplot`
- Catplot → `catplot`

## References

- Seaborn docs: https://seaborn.pydata.org/
- Matplotlib: https://matplotlib.org/

---

If you want, I can:
- Add runnable examples (small scripts or notebooks)
- Generate a short Jupyter notebook with these examples
- Commit changes to Git for you
