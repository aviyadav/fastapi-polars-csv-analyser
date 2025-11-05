import polars as pl
from fastapi import UploadFile, HTTPException
import os
from core.config import CURRENT_FILE, UPLOAD_DIR

async def save_and_read_csv(file: UploadFile) -> pl.DataFrame:
    """
    Save the uploaded CSV file to the upload directory and read it into a Polars DataFrame.

    Args:
        file (UploadFile): The uploaded CSV file.
    Returns:
        pl.DataFrame: The Polars DataFrame containing the CSV data.
    """
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    contents = await file.read()

    with open(CURRENT_FILE, "wb") as f:
        f.write(contents)

    return pl.read_csv(CURRENT_FILE)

def get_df(lazy: bool = False) -> pl.DataFrame | pl.LazyFrame:
    """
    Get a Polars DataFrame from the saved CSV file.

    Args:
        lazy (bool): If True, return a lazy DataFrame. Defaults to False.

    Returns:
        pl.DataFrame | pl.LazyFrame: The Polars DataFrame or LazyFrame containing the CSV data.
    """
    if not os.path.exists(CURRENT_FILE):
        raise HTTPException(
            status_code=404, detail="CSV file not found. Please upload a file first."
        )
    
    if lazy:
        return pl.scan_csv(CURRENT_FILE)
    return pl.read_csv(CURRENT_FILE)
