from fastapi import APIRouter, HTTPException
from services.eda import get_summary
from schemas.eda import SummaryResponse

router = APIRouter()

@router.get("/", response_model=SummaryResponse)
def summary():
    try:
        return get_summary()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))