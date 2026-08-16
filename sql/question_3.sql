-- Research Question 3
-- How does adjusted gross income (AGI) affect total tax liability?
-- Purpose: Compare average AGI and average tax liability across income groups.

SELECT
    [Size of Adjusted Gross Income],
    ROUND(AVG([Adjusted Gross Income (AGI)]), 2) AS AverageAGI,
    ROUND(AVG([Total Tax Liability (Amount)]), 2) AS AverageTaxLiability
FROM
    Clean_NoBlanks
WHERE
    [Size of Adjusted Gross Income] IS NOT NULL
    AND [Size of Adjusted Gross Income] <> 'Total'
GROUP BY
    [Size of Adjusted Gross Income];
