from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlmodel import Session
from app.utils import validate_file
from app.services.ocr import extract_text_from_pdf
from app.services.parser import parse_receipt_text
from app.crud import create_receipt
from app.db.database import get_session

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...), session: Session = Depends(get_session)):
    validate_file(file)
    contents = await file.read()
    text = extract_text_from_pdf(contents)
    parsed = parse_receipt_text(text)

    if not parsed:
        raise HTTPException(status_code=422, detail="Could not parse receipt data")

    receipt = create_receipt(session, parsed)
    return {"receipt": receipt}