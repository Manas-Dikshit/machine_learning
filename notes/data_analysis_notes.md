# Data distribution analysis, Outlier detection, Correlation analysis, Feature relationships

- [ ] Outlier detection
- [ ] Correlation analysis
- [ ] Feature relationships

This document contains concise, practical notes and runnable examples for EDA tasks commonly used in machine learning workflows.

## 1. Data distribution analysis

Purpose: understand each feature's distribution to detect skewness, multimodality, and appropriate preprocessing (scaling, transforms).

Core checks:

- Summary statistics: `df.describe()`
- Missing values: `df.isnull().sum()`
- Shape & dtypes: `df.info()`
- Skewness / kurtosis: `df.skew()`, `df.kurtosis()`

Visualizations (recommended):

- Histogram (`sns.histplot`) — use `kde=True` to overlay density
- KDE (`sns.kdeplot`) — good for smooth shape
- Boxplot / Violin (`sns.boxplot`, `sns.violinplot`) — highlight spread and outliers
- Rug + ECDF (`sns.rugplot`, `sns.ecdfplot`) — precise distribution tails

Example:

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
plt.figure(figsize=(10,4))
sns.histplot(df['age'].dropna(), kde=True)
plt.title('Age distribution')
plt.show()

plt.figure(figsize=(6,4))
sns.violinplot(x=df['fare'].dropna())
plt.title('Fare distribution (violin)')
plt.show()
```

When to transform:

- Strong right skew (long tail): consider `log1p`, `sqrt`, or Box–Cox (when positive)
- Bimodal / multimodal: investigate subgroups (use `hue` / `FacetGrid`)

Quick transform example:

```python
import numpy as np
df['fare_log1p'] = np.log1p(df['fare'].fillna(0))
sns.histplot(df['fare_log1p'], kde=True)
```

## 2. Outlier detection

Purpose: find extreme values that may distort models, especially those sensitive to scale (linear models, K-means).

Common methods:

- IQR rule (simple, robust): mark points outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR]
- Z-score (assumes normality): |z| > 3 often considered outlier
- Median Absolute Deviation (MAD): robust alternative to Z-score
- Model-based: `IsolationForest`, `LocalOutlierFactor` (unsupervised)

IQR example:

```python
Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df['age'] < lower) | (df['age'] > upper)]
len(outliers)
```

IsolationForest example:

```python
from sklearn.ensemble import IsolationForest
iso = IsolationForest(contamination=0.01, random_state=0)
mask = iso.fit_predict(df[['age','fare']].dropna())
# mask == -1 indicates outlier
```

Handling strategies:

- Investigate: verify whether value is valid (typo, measurement error)
- Trim / remove: drop extreme rows (only if justified)
- Cap (winsorize): replace beyond-threshold values with boundary values
- Transform: apply `log` or scaling to reduce influence
- Use robust models: tree-based models, robust scalers

Visualization to spot outliers:

- Boxplot grouped by category (`sns.boxplot(x='pclass', y='fare', data=df)`) — shows within-group outliers
- Scatter with alpha (`sns.scatterplot`) — reveals extreme pairs

## 3. Correlation analysis

Purpose: measure linear/non-linear associations, detect multicollinearity, and guide feature selection.

Numeric correlations:

- Pearson: linear correlation (sensitive to outliers)
- Spearman: rank correlation (captures monotonic relationships)
- Kendall: rank-based, robust for small samples

Compute correlation and plot:

```python
num = df.select_dtypes(include='number')
corr_pearson = num.corr(method='pearson')
plt.figure(figsize=(8,6))
sns.heatmap(corr_pearson, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Pearson correlation')
plt.show()
```

Categorical associations:

- Contingency tables + Chi-squared test for independence
- Cramér's V for strength of association

Example: Cramér's V (quick function):

```python
import numpy as np
import scipy.stats as ss

def cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r,k = confusion_matrix.shape
    return np.sqrt(phi2 / min(k-1, r-1))
```

Multicollinearity checks:

- Variance Inflation Factor (VIF) to detect redundant predictors

VIF example (use `statsmodels`):

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor
X = num.dropna()
vif = pd.DataFrame({'feature': X.columns,
                    'VIF': [variance_inflation_factor(X.values, i)
                            for i in range(X.shape[1])]})
print(vif)
```

When to act on correlation:

- If two features are highly correlated (e.g., |r| > 0.85), consider dropping one, combining them, or using regularization.

## 4. Feature relationships

Purpose: explore pairwise and conditional relationships between features and target to inform feature engineering and model choice.

Useful visualizations:

- Scatter + regression (`sns.scatterplot`, `sns.regplot`) for numeric vs numeric
- Joint plots (`sns.jointplot`) for combined scatter + marginals
- Pair plots (`sns.pairplot`) to inspect many pairwise interactions
- Box/violin/point plots for numeric vs categorical
- FacetGrid for conditional relationships across categories

Examples:

Numeric vs numeric (with regression):

```python
sns.regplot(data=df, x='age', y='fare', scatter_kws={'alpha':0.4})
plt.title('Age vs Fare with regression fit')
```

Categorical vs numeric:

```python
sns.boxplot(data=df, x='pclass', y='fare')
sns.pointplot(data=df, x='pclass', y='survived', ci=95)
```

Conditional relationships / interactions:

- Use `hue` to add a third variable (e.g., `hue='sex'`)
- Use `FacetGrid` to split plots by another categorical variable

Example — interaction via FacetGrid:

```python
g = sns.FacetGrid(df, col='sex', row='pclass', height=3)
g.map(sns.scatterplot, 'age', 'fare', alpha=0.6)
```

Feature engineering suggestions based on relationships:

- Create interaction features when two features jointly explain variance (e.g., `age*income`)
- Binning numeric variables if relationship is non-linear (e.g., `pd.qcut`) and use as categorical
- Encode categorical variables appropriately (one-hot, target encoding) depending on model

## Tips & pitfalls

- Always visualize before removing data — outliers can be meaningful.
- Beware of using Pearson when non-linear relationships exist.
- When using log transforms, handle zeros/negatives (`log1p` for zeros).
- Use cross-validation when validating preprocessing choices.

## Next steps (optional)

- I can convert these notes into a Jupyter notebook with runnable cells.
- I can add code to compute VIF and automatically flag features with high multicollinearity.
