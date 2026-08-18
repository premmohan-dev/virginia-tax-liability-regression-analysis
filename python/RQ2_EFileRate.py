# Purpose:
# Visualize electronic filing rates across income groups.

# Research Question 2
# How do electronic filing rates vary across income groups and ZIP codes?

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

# Electronic Filing Rates (%)
efile_rates = [
    92.28,
    94.37,
    94.03,
    93.55,
    93.45,
    94.27
]

# Create Chart
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(
    income_groups,
    efile_rates,
    color="steelblue"
)

ax.set_title("Electronic Filing Rate by Income Group")
ax.set_xlabel("Size of Adjusted Gross Income")
ax.set_ylabel("Electronic Filing Rate (%)")

# Add Data Labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f"{height:.2f}%",
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 3),
        textcoords="offset points",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()
