"""
Main ETL Pipeline
"""

from extract import extract_data
from transform import clean_data
from validation import validate_data
from analytics import calculate_metrics
from load import (
    load_to_sql,
    export_summary
)

from logger import get_logger

logger = get_logger()


def main():

    logger.info("=" * 60)

    logger.info("PIPELINE STARTED")

    # --------------------------------

    market_data = extract_data()

    print("\nRaw Data")

    print(market_data.head())

    print("\nShape")

    print(market_data.shape)

    # --------------------------------

    market_data_clean = clean_data(

        market_data

    )

    print("\nClean Data")

    print(market_data_clean.head())

    # --------------------------------

    validate_data(

        market_data_clean

    )

    # --------------------------------

    (

        market_data_clean,

        summary_table,

        performance_ranking,

        top_gainer,

        top_loser

    ) = calculate_metrics(

        market_data_clean

    )

    # --------------------------------

    load_to_sql(

        market_data_clean

    )

    export_summary(

        summary_table

    )

    # --------------------------------

    print("\nPerformance Ranking")

    print(performance_ranking)

    print("\nTop Gainer")

    print(top_gainer)

    print("\nTop Loser")

    print(top_loser)

    print("\nSummary Table")

    print(summary_table)

    logger.info("PIPELINE COMPLETED")

    logger.info("=" * 60)


if __name__ == "__main__":

    main()