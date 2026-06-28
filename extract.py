"""
Extract Module
--------------
Downloads stock market data from Yahoo Finance.
"""

import pandas as pd
import yfinance as yf

from config import (
    STOCKS,
    PERIOD,
    RAW_DATA_PATH
)

from logger import get_logger

logger = get_logger()


def extract_data() -> pd.DataFrame:
    """
    Downloads historical stock data.

    Returns
    -------
    pandas.DataFrame
        Combined stock market data.
    """

    logger.info("Starting data extraction.")

    all_data = []

    try:

        for stock in STOCKS:

            logger.info(f"Downloading {stock}")

            data = yf.Ticker(stock).history(
                period=PERIOD
            )

            data["Stock_Name"] = stock

            all_data.append(data)

        market_data = pd.concat(
            all_data,
            ignore_index=False
        )

        market_data = market_data.reset_index()

        market_data.to_csv(
            RAW_DATA_PATH,
            index=False
        )

        logger.info(
            "Raw data saved successfully."
        )

        logger.info(
            "Data extraction completed."
        )

        return market_data

    except Exception as error:

        logger.exception(
            f"Extraction Failed : {error}"
        )

        raise