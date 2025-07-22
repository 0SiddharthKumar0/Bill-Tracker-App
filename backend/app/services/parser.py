import re
from datetime import datetime
from typing import Optional
from app.models import ReceiptCreate

def parse_receipt_text(text: str) -> Optional[ReceiptCreate]:
    vendor = "Unknown"
    amount = None
    date = None

    amount_match = re.search(r"(?:Total|Amount)[^\d]*(\d+\.\d{2})", text, re.IGNORECASE)
    if amount_match:
        amount = float(amount_match.group(1))

    date_match = re.search(r"(\d{2}/\d{2}/\d{4})", text)
    if date_match:
        date = datetime.strptime(date_match.group(1), "%d/%m/%Y").date()

    lines = text.splitlines()
    for line in lines:
        if line.strip() and len(line.strip()) < 25:
            vendor = line.strip()
            break

    if amount and date:
        return ReceiptCreate(vendor=vendor, amount=amount, category=None, date=date)
    return None