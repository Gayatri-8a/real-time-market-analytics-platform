"""
Analytics Module
----------------
Calculates business metrics from stock market data.
"""

import pandas as pd

from logger import get_logger

logger = get_logger()


def calculate_metrics(
    market_data_clean: pd.DataFrame
):

    logger.info("Calculating business metrics.")

    market_data_clean["Daily_Return"] = (

        market_data_clean

        .groupby("Stock_Name")["Close_Price"]

        .pct_change() * 100

    )

    summary_table = (

        market_data_clean

        .groupby("Stock_Name")

        .agg(

            Average_Return=("Daily_Return", "mean"),

            Average_Volume=("Volume", "mean"),

            Highest_Price=("High_Price", "max"),

            Lowest_Price=("Low_Price", "min"),

            Volatility=("Daily_Return", "std")

        )

    )

    performance_ranking = (

        summary_table["Average_Return"]

        .sort_values(

            ascending=False

        )

    )

    top_gainer = performance_ranking.idxmax()

    top_loser = performance_ranking.idxmin()

    logger.info("Analytics completed.")

    return (

        market_data_clean,

        summary_table,

        performance_ranking,

        top_gainer,

        top_loser

    )