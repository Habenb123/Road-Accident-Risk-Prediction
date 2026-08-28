import sys

import pandas as pd

from src.exception import CustomException
from src.logger import logger


def load_raw_data(path: str) -> pd.DataFrame:
    try:
        logger.info("Starting STATS19 data ingestion")

        df = pd.read_csv(path)

        logger.info(
            f"Loaded {df.shape[0]} rows and {df.shape[1]} columns"
        )

        return df

    except Exception as e:
        logger.error("Error occurred during STATS19 data ingestion")
        raise CustomException(e, sys) from e