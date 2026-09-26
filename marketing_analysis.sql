USE CustomerChurn;

SELECT COUNT(*) as TotalCustomers
from dbo.marketing_data; 

SELECT 
    COUNT(*) as totalrows, 
    COUNT(ID) as ID_NotNull,
    COUNT(Income) as Income_NotNull,
    COUNT(Education) as Education_NotNull,
    COUNT(Marital_Status) as Maritalstatus_NotNull
from dbo.marketing_data;


SELECT
    COUNT(ID) AS totalIDs, 
    COUNT(distinct ID) AS UniqueIDs
FROM dbo.marketing_data; 

SELECT 
    Education, 
    COUNT(*) as CustomerCount
from dbo.marketing_data
GROUP BY Education
ORDER BY CustomerCount DESC;

SELECT
    Marital_Status,
    COUNT(*) as CustomerCount
FROM dbo.marketing_data
GROUP BY Marital_Status
ORDER BY CustomerCount DESC;

SELECT
    MIN(Income) as MinimumIncome,
    MAX(Income) as MaxIncome,
    AVG(Income) as AverageIncome
from dbo.marketing_data;

SELECT
    MIN(Year_Birth) as Oldestbirthyear,
    MAX(Year_Birth) as youngestbirthyear,
    AVG(Year_Birth) as averagebirthyear
FROM dbo.marketing_data;

SELECT
    COUNT(*) as totalinside
FROM dbo.marketing_data

SELECT top 5 *
from dbo.marketing_data

SELECT
    SUM(MntWines) as winespending,
    SUM(MntFruits) as fruitspending,
    SUM(MntMeatProducts) as meatspending,
    SUM(MntFishProducts) as fishspending,
    SUM(MntSweetProducts) as Sweetspending,
    SUM(MntGoldProds) as goldspending
from dbo.marketing_data;

SELECT
    AVG(MntWines) as avgwinespending,
    AVG(MntFruits) as avgfruitspending,
    AVG(MntMeatProducts) as avgmeatspending,
    AVG(MntFishProducts) as avgfishspending,
    AVG(MntSweetProducts) as avgSweetspending,
    AVG(MntGoldProds) as avggoldspending
from dbo.marketing_data;

SELECT
    ID,
    MntWines + MntFruits + MntMeatProducts + mntfishproducts + mntsweetproducts + mntgoldprods as TotalSpending
from dbo.marketing_data
ORDER BY TotalSpending DESC;

SELECT TOP 10
    ID,
    Income,
    Education,
    Marital_Status,
    Year_Birth,
    MntWines,
    MntFruits,
    MntMeatProducts,
    MntFishProducts,
    MntSweetProducts,
    MntGoldProds,
    NumWebPurchases,
    NumCatalogPurchases,
    NumStorePurchases
FROM dbo.marketing_data
ORDER BY
    MntWines + MntFruits + MntMeatProducts +
    MntFishProducts + MntSweetProducts + MntGoldProds DESC;

   SELECT
    SUM(CAST(AcceptedCmp1 AS INT)) AS Campaign1Accepted,
    SUM(CAST(AcceptedCmp2 AS INT)) AS Campaign2Accepted,
    SUM(CAST(AcceptedCmp3 AS INT)) AS Campaign3Accepted,
    SUM(CAST(AcceptedCmp4 AS INT)) AS Campaign4Accepted,
    SUM(CAST(AcceptedCmp5 AS INT)) AS Campaign5Accepted,
    SUM(CAST(Response AS INT)) AS ResponseAccepted
FROM dbo.marketing_data;

SELECT
    SUM(CAST(AcceptedCmp1 AS INT)) * 100.0 / COUNT(*) AS Campaign1Rate
FROM dbo.marketing_data;

SELECT
    SUM(CAST(AcceptedCmp1 AS INT)) * 100.0 / COUNT(*) AS Campaign1Rate,
    SUM(CAST(AcceptedCmp2 AS INT)) * 100.0 / COUNT(*) AS Campaign2Rate,
    SUM(CAST(AcceptedCmp3 AS INT)) * 100.0 / COUNT(*) AS Campaign3Rate,
    SUM(CAST(AcceptedCmp4 AS INT)) * 100.0 / COUNT(*) AS Campaign4Rate,
    SUM(CAST(AcceptedCmp5 AS INT)) * 100.0 / COUNT(*) AS Campaign5Rate,
    SUM(CAST(Response AS INT)) * 100.0 / COUNT(*) AS ResponseRate
FROM dbo.marketing_data;

SELECT
    ID,
    Income,
    case 
        when Income < 3000 then 'Low Income'
        when Income < 6000 then 'Medium Income'
        else 'Hıgh Income'
    end as IncomeSegment
from dbo.marketing_data;


use CustomerChurn;
SELECT
    
    case 
        when Income < 3000 then 'Low Income'
        when Income < 6000 then 'Medium Income'
        else 'High Income'
    end as IncomeSegment,
    COUNT(*) as CustomerCount 
from dbo.marketing_data
GROUP BY
    case 
        when Income < 3000 then 'Low Income'
        when Income < 6000 then 'Medium Income'
        else 'High Income'
    END
ORDER BY CustomerCount DESC;


WITH IncomeGroups AS (
    SELECT
        ID,
        Income,
        NTILE(4) OVER (ORDER BY Income) AS IncomeQuartile
    FROM dbo.marketing_data
    WHERE Income IS NOT NULL
)
SELECT
    IncomeQuartile,
    COUNT(*) AS CustomerCount,
    MIN(Income) AS MinIncome,
    MAX(Income) AS MaxIncome
FROM IncomeGroups
GROUP BY IncomeQuartile
ORDER BY IncomeQuartile;

SELECT
    ID,
    Income
FROM dbo.marketing_data
WHERE Income >= 100000
ORDER BY Income DESC;

WITH IncomeGroups AS (
    SELECT
        ID,
        Income,
        NTILE(4) OVER (ORDER BY Income) AS IncomeQuartile
    FROM dbo.marketing_data
    WHERE Income IS NOT NULL
)
SELECT
    IncomeQuartile,
    COUNT(*) AS CustomerCount,
    SUM(CAST(AcceptedCmp4 AS INT)) AS Campaign4Accepted,
    SUM(CAST(AcceptedCmp4 AS INT)) * 100.0 / COUNT(*) AS Campaign4Rate
FROM IncomeGroups
JOIN dbo.marketing_data
    ON IncomeGroups.ID = dbo.marketing_data.ID
GROUP BY IncomeQuartile
ORDER BY IncomeQuartile;