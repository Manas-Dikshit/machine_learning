
# Linear Regression — Concise Notes

## What it is
Linear regression models the relationship between a dependent variable $y$ and one or more independent variables $x$ by fitting a linear function. The simple (one-variable) form is:
$$
y = \beta_0 + \beta_1 x + \varepsilon
$$
where $\beta_0$ is the intercept, $\beta_1$ the slope, and $\varepsilon$ noise.

## Goal
Estimate coefficients $\beta$ so predictions $\hat{y}$ generalize to new data, minimizing a loss (commonly mean squared error).

## Types
- Simple linear regression: one predictor.
- Multiple linear regression: many predictors, written in matrix form $\mathbf{y}=X\beta+\varepsilon$.

## Loss and solutions
- Loss (MSE): $\mathrm{MSE}=\frac{1}{n}\sum_{i}(y_i-\hat y_i)^2$.
- Normal equation (closed form):
$$
\hat{\beta}=(X^TX)^{-1}X^Ty
$$
provided $X^TX$ is invertible.
- Iterative optimization: gradient descent (useful for large or ill-conditioned $X$).

## Assumptions (classical linear regression)
- Linearity: relationship is linear in parameters.
- Independence: residuals are independent.
- Homoscedasticity: constant variance of residuals.
- Normality (for inference): residuals are approximately normal.
- No (or low) multicollinearity among predictors.

## Evaluation
- R-squared: proportion of variance explained.
- RMSE / MSE: typical prediction error scale.
- Residual analysis: check patterns, heteroscedasticity, outliers.

## Simple examples
Normal-equation with NumPy:

```python
import numpy as np
X = np.c_[np.ones(len(x)), x]  # add intercept column
beta_hat = np.linalg.inv(X.T @ X) @ X.T @ y
```

Using scikit-learn:

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X_train, y_train)
preds = model.predict(X_test)
```

## Practical notes
- Scale features for gradient-based solvers.
- Regularization (Ridge/Lasso) helps with multicollinearity and overfitting.
- Always inspect residuals and validate on held-out data.

## Next steps
- Try a worked example with a small dataset, plot fit and residuals.

y = mx + c
m = slope
c = y intercept