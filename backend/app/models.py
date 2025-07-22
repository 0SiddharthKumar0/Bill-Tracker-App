from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional

class Receipt(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    vendor: str
    amount: float
    category: Optional[str] = None
    date: date

class ReceiptCreate(SQLModel):
    vendor: str
    amount: float
    category: Optional[str] = None
    date: date