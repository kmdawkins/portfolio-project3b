import pandas as pd
from loguru import logger

def load_csv_with_fallback(path: str, delimiters: list = [",", ";", "\t"]) -> pd.DataFrame:
    """
    Try loading a CSV using multiple delimiters.
    Returns the DataFrame if successful, otherwise raises an exception.
    """
    for delimiter in delimiters:
        try:
            df = pd.read_csv(path, delimiter=delimiter, on_bad_lines="error")

            # ✅ Additional checks to ensure usable structure
            if df.empty:
                raise ValueError(f"No data loaded using delimiter '{delimiter}'.")
            if df.shape[1] < 2:
                raise ValueError(f"Too few columns with delimiter '{delimiter}'.")

            logger.info(f"✅ Loaded CSV using delimiter: '{delimiter}' with {len(df)} rows.")
            return df

        except Exception as e:
            logger.warning(f"⚠️ Failed to load with delimiter '{delimiter}': {e}")

    logger.error("❌ All delimiter attempts failed. Check file format.")
    raise ValueError("Unable to read CSV with provided delimiters.")
