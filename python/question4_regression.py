# Purpose:
# Evaluate how well adjusted gross income (AGI) predicts total tax liability
# using a linear regression model.

# Research Question 4
# How well does the regression model explain variation in total tax liability?

# Import Libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load Data
df = xl("A1:G6333", headers=True)

# Remove completely blank separator rows
df = df.dropna(how="all")

# Keep ZIP-level totals only
zip_totals = df[df["Size of Adjusted Gross Income"].isna()]

# Create Regression Variables
X = zip_totals[["Adjusted Gross Income (AGI)"]]
y = zip_totals["Total Tax Liability (Amount)"]

# Build Regression Model
model = LinearRegression()
model.fit(X, y)

# Model Results
r_squared = model.score(X, y)

print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])
print("R-squared:", r_squared)
