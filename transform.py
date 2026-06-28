"""
Transform Module
----------------
Cleans and prepares raw stock market data.
"""

import pandas as pd

from config import PROCESSED_DATA_PATH
from logger import get_logger

logger = get_logger()


def clean_data(market_data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the extracted stock market data.

    Parameters
    ----------
    market_data : pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """

    logger.info("Starting data transformation.")

    market_data_clean = market_data[
        [
            "Date",
            "Stock_Name",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume"
        ]
    ].copy()

    market_data_clean.rename(
        columns={
            "Open": "Open_Price",
            "High": "High_Price",
            "Low": "Low_Price",
            "Close": "Close_Price"
        },
        inplace=True
    )

    market_data_clean["Date"] = (
        market_data_clean["Date"]
        .dt.tz_localize(None)
    )

    market_data_clean.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )

    logger.info("Processed data saved successfully.")

    logger.info("Transformation completed.")

    return market_data_clean