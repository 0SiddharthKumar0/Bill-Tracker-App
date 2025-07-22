from sqlmodel import Session, select
from app.models import Receipt

def get_all_receipts(session: Session):
    return session.exec(select(Receipt)).all()

def create_receipt(session: Session, receipt: Receipt):
    session.add(receipt)
    session.commit()
    session.refresh(receipt)
    return receipt
