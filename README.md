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

### Key Findings

Average tax liability increased across each Size of Adjusted Gross Income category. The $200,000 or more income group reported the highest average tax liability at approximately $103,950.25, while the $1 under $25,000 income group reported the lowest at approximately $1,094.93. As income levels increased, average tax liability generally increased as well, indicating a strong positive relationship between income level and tax liability across Virginia ZIP codes.

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
