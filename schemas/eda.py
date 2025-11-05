from pydantic import BaseModel
from typing import List

class ColumnSummary(BaseModel):
    column: str
    dtype: str
    missing: int
    unique: int


class SummaryResponse(BaseModel):
    num_rows: int
    num_columns: int
    columns: List[ColumnSummary]