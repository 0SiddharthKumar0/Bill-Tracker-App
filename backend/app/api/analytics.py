from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.crud import get_all_receipts
from app.db.database import get_session


router = APIRouter()

@router.get("/")
def get_receipts(session: Session = Depends(get_session)):
    return get_all_receipts(session)