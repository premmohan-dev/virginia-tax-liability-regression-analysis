-- Research Question 1
-- How does total tax liability vary across income groups in Virginia?
-- Purpose: Compare average and total tax liability across income groups.

SELECT
    [Size of Adjusted Gross Income],
    ROUND(AVG([Total Tax Liability (Amount)]), 2) AS AverageTaxLiability,
    SUM([Total Tax Liability (Amount)]) AS TotalTaxLiability
FROM
    Clean_NoBlanks
WHERE
    [Size of Adjusted Gross Income] IS NOT NULL
    AND [Size of Adjusted Gross Income] <> 'Total'
GROUP BY
    [Size of Adjusted Gross Income];
