USE MarketAnalyticsDB;
GO

-- ==========================================
-- Daily Stock Data View
-- ==========================================

CREATE OR ALTER VIEW vw_Daily_Stock_Data AS

SELECT

    Date,

    Stock_Name,

    Open_Price,

    High_Price,

    Low_Price,

    Close_Price,

    Volume,

    Daily_Return

FROM Market_Data;

GO

-- ==========================================
-- Stock Performance Summary View
-- ==========================================

CREATE OR ALTER VIEW vw_Stock_Performance AS

SELECT

    Stock_Name,

    AVG(Daily_Return) AS Average_Return,

    AVG(Volume) AS Average_Volume,

    MAX(High_Price) AS Highest_Price,

    MIN(Low_Price) AS Lowest_Price,

    STDEV(Daily_Return) AS Volatility

FROM Market_Data

GROUP BY Stock_Name;

GO