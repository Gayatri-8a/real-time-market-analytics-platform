"""
Logger Module
-------------
Creates a project-wide logger.
"""

import logging
import os

from config import LOG_FILE

# Create logs directory automatically
os.makedirs("logs", exist_ok=True)

logging.basicConfig(

    filename=LOG_FILE,

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s",

    filemode="a"

)


def get_logger():
    """
    Returns the configured logger.
    """

    return logging.getLogger("MarketAnalysis")