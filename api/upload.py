from fastapi import APIRouter, UploadFile, File, HTTPException
from services.file_processing import save_and_read_csv

router = APIRouter()

@router.post("/")
async def upload_csv(file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file type. Only CSV files are accepted.")

    try:
        df = await save_and_read_csv(file)
        return {
            "message": "File uploaded and parsed successfully",
            "columns": df.columns,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {e}")