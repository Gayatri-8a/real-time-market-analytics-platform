"""
Project Configuration File
--------------------------
Stores all configurable settings used across the ETL pipeline.
"""

# ==========================================
# STOCK CONFIGURATION
# ==========================================

STOCKS = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS"
]

# Historical period

PERIOD = "1y"

# ==========================================
# DATABASE CONFIGURATION
# ==========================================

SERVER = r"localhost\SQLEXPRESS"

DATABASE = "MarketAnalyticsDB"

TABLE_NAME = "Market_Data"

# ==========================================
# FILE PATHS
# ==========================================

RAW_DATA_PATH = "data/raw/raw_market_data.csv"

PROCESSED_DATA_PATH = "data/processed/processed_market_data.csv"

SUMMARY_PATH = "output/summary_table.csv"

LOG_FILE = "logs/pipeline.log"