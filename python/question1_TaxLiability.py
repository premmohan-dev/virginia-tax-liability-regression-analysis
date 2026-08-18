# Purpose:
# Visualize average tax liability across Size of Adjusted Gross Income categories.

# Research Question 1
# How does total tax liability vary across income groups in Virginia?

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Income Groups
income_groups = [
    "1-25K",
    "25K-50K",
    "50K-75K",
    "75K-100K",
    "100K-200K",
    "200K+"
]

# Average Tax Liability Values
average_tax_liability = [
    1094.93,
    4975.83,
    7601.66,
    8692.86,
    32591.72,
    103950.25
]

# Create Chart
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(
    income_groups,
    average_tax_liability,
    color="steelblue"
)

ax.set_title("Average Tax Liability by Income Group")
ax.set_xlabel("Size of Adjusted Gross Income")
ax.set_ylabel("Average Tax Liability (Amount)")

# Add Data Labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f"{height:,.0f}",
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 3),
        textcoords="offset points",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()
