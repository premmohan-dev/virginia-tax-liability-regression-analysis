# Virginia Tax Liability Regression Analysis

## Overview

This analysis uses IRS Statistics of Income (SOI) data from Tax Year 2021 to examine the relationship between adjusted gross income (AGI), taxable income, and total tax liability across Virginia ZIP codes and income groups through regression analysis.

## Objectives

- Analyze Virginia tax return data across ZIP codes and income groups.
- Examine how total tax liability varies across adjusted gross income (AGI) categories.
- Explore electronic filing patterns among Virginia taxpayers.
- Build a regression model to evaluate the relationship between income measures and total tax liability.
- Identify factors associated with variations in tax liability across Virginia ZIP codes and income groups.

## Dataset

This analysis uses IRS Statistics of Income (SOI) data from **VIRGINIA Individual Income Tax Returns: Selected Income and Tax Items by State, ZIP Code, and Size of Adjusted Gross Income, Tax Year 2021**.

The dataset contains Virginia ZIP code-level tax return data grouped by adjusted gross income (AGI) ranges. For each ZIP code and income group, the dataset reports measures such as the number of returns, electronically filed returns, adjusted gross income, taxable income, and total tax liability.

> **Note:** Monetary values in the dataset are reported in thousands of dollars.

Source: IRS Statistics of Income (SOI) Division, Individual Master File System, February 2024.

The cleaned dataset used in this analysis includes:

- ZIP Code
- Size of Adjusted Gross Income
- Number of Returns
- Number of Electronically Filed Returns
- Adjusted Gross Income (AGI)
- Taxable Income
- Total Tax Liability

## Research Questions

1. How does total tax liability vary across income groups in Virginia?
2. How do electronic filing rates vary across income groups and ZIP codes?
3. How does adjusted gross income (AGI) affect total tax liability?
4. How well does the regression model explain variation in total tax liability?

## Research Question 1

### How does total tax liability vary across income groups in Virginia?

<img width="989" height="590" alt="RQ1_TaxLiabilityByIncomeGroup" src="https://github.com/user-attachments/assets/3b109168-509a-460e-ba3c-7156aeca3486" />

### Key Findings

Average tax liability increased across each Size of Adjusted Gross Income category. The $200,000 or more income group reported the highest average tax liability at approximately $103,950.25, while the $1 under $25,000 income group reported the lowest at approximately $1,094.93. As income levels increased, average tax liability increased as well, indicating a strong positive relationship between income level and tax liability across Virginia ZIP codes.

## Research Question 2

### How do electronic filing rates vary across income groups and ZIP codes?

<img width="989" height="590" alt="RQ2_EFileRate" src="https://github.com/user-attachments/assets/1c766b0f-8450-435f-9916-bb5bd88b0228" />

### Key Findings

Electronic filing rates remained consistently high across all Size of Adjusted Gross Income categories, ranging from 92.28% to 94.37%. The $25,000 under $50,000 income group reported the highest electronic filing rate at 94.37%, while the $1 under $25,000 category reported the lowest at 92.28%. Overall, more than 90% of returns were filed electronically across every income group, suggesting widespread adoption of electronic filing regardless of income.

## Research Question 3

### How does adjusted gross income (AGI) affect total tax liability?

| Income Group | Average AGI | Average Tax Liability |
|-------------|------------:|----------------------:|
| 1-25K | $34,434.59 | $1,094.93 |
| 25K-50K | $81,537.05 | $4,975.83 |
| 50K-75K | $88,708.61 | $7,601.66 |
| 75K-100K | $85,417.15 | $8,692.86 |
| 100K-200K | $256,254.74 | $32,591.72 |
| 200K+ | $471,769.02 | $103,950.25 |

### Key Findings

Average adjusted gross income (AGI) and average tax liability both increased across the Size of Adjusted Gross Income categories. The $200,000 or more income group had the highest average AGI at $471,769.02 and the highest average tax liability at $103,950.25. Meanwhile, the $1 under $25,000 category had the lowest average AGI at $34,434.59 and the lowest average tax liability at $1,094.93. Overall, the results suggest a strong positive relationship between AGI and total tax liability across Virginia ZIP codes.

## Research Question 4

### How well does the regression model explain variation in total tax liability?

<img width="689" height="556" alt="RQ4_AGI_Regression_Model" src="https://github.com/user-attachments/assets/e031d844-72bc-4a97-8635-125dfba4ec60" />

### Key Findings

The linear regression model produced an R² value of 0.9415, meaning that approximately 94.15% of the variation in total tax liability is explained by adjusted gross income (AGI). The model also produced a positive slope of 0.1873, showing that higher AGI values are associated with higher tax liability. These results indicate that AGI is a highly effective predictor of total tax liability within the Virginia ZIP code data.

## Methods

- Data cleaning and preparation
- SQL analysis
- Exploratory data
- Data visualization
- Regression modeling

## Tools and Technologies

- Microsoft Excel
- Microsoft Access
- SQL
- Python
- Pandas
- Matplotlib
- Scikit-learn

## SQL Analysis

The SQL queries included in this analysis were developed and tested in Microsoft Access. These queries were used to clean the dataset, calculate descriptive statistics, compare tax liability across income groups, evaluate electronic filing rates, and examine the relationship between adjusted gross income (AGI) and total tax liability. SQL served as the primary tool for preparing and summarizing the data prior to visualization and regression modeling.

## Conclusion

Overall, this analysis found that tax liability generally increased as income levels increased across Virginia ZIP codes and income groups. Electronic filing rates remained consistently high across all income categories, indicating widespread adoption of electronic filing regardless of income level. The regression analysis produced an R² value of 0.9415, showing that adjusted gross income (AGI) is a strong predictor of total tax liability. Together, these findings highlight the close relationship between income and tax liability within the Virginia tax return data.

## How to Use This Project

1. Review the original IRS Statistics of Income (SOI) dataset (`Virginia Tax Data 2021 Raw.xlsx`) included in the `data` folder.
2. Use the cleaned `Virginia Tax Data 2021 Cleaned.xlsx` dataset for analysis.
3. Import the dataset into Microsoft Access and run the SQL queries in the `sql` folder to perform data preparation and answer Research Questions 1 through 3.
4. Run the Python files in the `python` folder to generate visualizations and perform the regression analysis for Research Question 4.
5. Review the charts, table, and findings to understand how income levels, electronic filing rates, and tax liability vary across Virginia ZIP codes and income groups.
