-- ==========================================
-- Create Database
-- ==========================================

IF DB_ID('MarketAnalyticsDB') IS NULL
BEGIN
    CREATE DATABASE MarketAnalyticsDB;
END;
GO

USE MarketAnalyticsDB;
GO

-- ==========================================
-- Drop Existing Table
-- ==========================================

IF OBJECT_ID('dbo.Market_Data', 'U') IS NOT NULL
DROP TABLE dbo.Market_Data;
GO

-- ==========================================
-- Create Market_Data Table
-- ==========================================

CREATE TABLE dbo.Market_Data
(
    Market_ID INT IDENTITY(1,1) PRIMARY KEY,

    Date DATE NOT NULL,

    Stock_Name VARCHAR(50) NOT NULL,

    Open_Price FLOAT NOT NULL,

    High_Price FLOAT NOT NULL,

    Low_Price FLOAT NOT NULL,

    Close_Price FLOAT NOT NULL,

    Volume BIGINT NOT NULL,

    Daily_Return FLOAT NULL,

    Created_At DATETIME DEFAULT GETDATE()
);
GO

-- ==========================================
-- Prevent Duplicate Records
-- ==========================================

ALTER TABLE dbo.Market_Data
ADD CONSTRAINT UQ_MarketData
UNIQUE(Date, Stock_Name);
GO