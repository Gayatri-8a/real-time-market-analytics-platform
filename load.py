"""
Load Module
-----------
Loads processed data into SQL Server
using Incremental Loading.
"""

import pandas as pd

from sqlalchemy import create_engine

from config import (
    SERVER,
    DATABASE,
    TABLE_NAME,
    SUMMARY_PATH
)

from logger import get_logger

logger = get_logger()


def create_sql_engine():

    connection_string = (
        f"mssql+pyodbc://@{SERVER}/{DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&trusted_connection=yes"
    )

    return create_engine(connection_string)


def load_to_sql(df):

    try:

        logger.info("Starting Incremental Load.")

        engine = create_sql_engine()

        # -----------------------------------
        # Read Existing SQL Data
        # -----------------------------------

        try:

            existing_df = pd.read_sql(

                f"SELECT Date, Stock_Name FROM {TABLE_NAME}",

                engine

            )

        except:

            existing_df = pd.DataFrame(
                columns=["Date", "Stock_Name"]
            )

        # -----------------------------------
        # Find New Records
        # -----------------------------------

        if len(existing_df) > 0:

            existing_keys = set(

                zip(

                    existing_df["Date"],

                    existing_df["Stock_Name"]

                )

            )

            new_df = df[

                ~df.apply(

                    lambda row:

                    (row["Date"], row["Stock_Name"])

                    in existing_keys,

                    axis=1

                )

            ]

        else:

            new_df = df

        # -----------------------------------
        # Insert Only New Rows
        # -----------------------------------

        if len(new_df) > 0:

            new_df.to_sql(

                TABLE_NAME,

                engine,

                if_exists="append",

                index=False

            )

            print(f"\n{len(new_df)} New Records Inserted.")

            logger.info(

                f"{len(new_df)} rows inserted."

            )

        else:

            print("\nNo New Records Found.")

            logger.info(

                "No new records."

            )

    except Exception as error:

        logger.exception(error)

        raise


def export_summary(summary_table):

    summary_table.to_csv(

        SUMMARY_PATH

    )

    logger.info(

        "Summary CSV Exported."

    )