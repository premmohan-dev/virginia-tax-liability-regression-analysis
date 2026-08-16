-- Data Preparation
-- Purpose: Removes fully blank separator rows from the imported dataset.

SELECT
    *
FROM
    Cleaned
WHERE
    [ZIP Code] IS NOT NULL;
