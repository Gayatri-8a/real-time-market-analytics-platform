"""
Validation Module
-----------------
Validates cleaned stock market data.
"""

import pandas as pd

from logger import get_logger

logger = get_logger()


def validate_data(df: pd.DataFrame) -> None:
    """
    Performs quality checks on data.
    """

    logger.info("Starting data validation.")

    missing_values = df.isnull().sum().sum()

    duplicate_rows = df.duplicated().sum()

    negative_open = (df["Open_Price"] < 0).sum()

    negative_close = (df["Close_Price"] < 0).sum()

    negative_volume = (df["Volume"] < 0).sum()

    invalid_high_low = (
        df["High_Price"] < df["Low_Price"]
    ).sum()

    print("\n========== DATA VALIDATION ==========")

    print(f"Missing Values : {missing_values}")

    print(f"Duplicate Rows : {duplicate_rows}")

    print(f"Negative Open Prices : {negative_open}")

    print(f"Negative Close Prices : {negative_close}")

    print(f"Negative Volumes : {negative_volume}")

    print(f"Invalid High-Low Records : {invalid_high_low}")

    logger.info("Validation completed successfully.")