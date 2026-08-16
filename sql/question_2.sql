-- Research Question 2
-- How do electronic filing rates vary across income groups and ZIP codes?
-- Purpose: Calculate e-file rates by income group.

SELECT
    [Size of Adjusted Gross Income],
    SUM([Number of Electronically Filed Returns]) AS TotalEFiledReturns,
    SUM([Number of Returns]) AS TotalReturns,
    ROUND(
        SUM([Number of Electronically Filed Returns]) /
        SUM([Number of Returns]) * 100,
        2
    ) AS EFileRatePercent
FROM
    Clean_NoBlanks
WHERE
    [Size of Adjusted Gross Income] IS NOT NULL
    AND [Size of Adjusted Gross Income] <> 'Total'
GROUP BY
    [Size of Adjusted Gross Income];
