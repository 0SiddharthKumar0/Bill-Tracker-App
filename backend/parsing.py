import re
from typing import Dict

def parse_receipt_text(text: str) -> Dict:
    # Heuristic regex (can be improved as needed)
    vendor_match = re.search(r'(?:from|vendor|biller|store):?\s*([^\n]+)', text, re.IGNORECASE)
    date_match = re.search(r'(\d{4}[-/]\d{2}[-/]\d{2}|\d{2}[-/]\d{2}[-/]\d{4})', text)
    amount_match = re.search(r'(?:amount\s*[:\-]?\s*|\₹|\$|USD)\s*([\d,.]+)', text, re.IGNORECASE)

    vendor = vendor_match.group(1).strip() if vendor_match else "Unknown"
    date = date_match.group(1) if date_match else "Unknown"
    amount = float(amount_match.group(1).replace(',', '')) if amount_match else 0.0

    # Optional category mapping (e.g., by vendor name)
    keywords = {"electricity": "Utilities", "internet": "Utilities", "grocery": "Groceries"}
    category = "Other"
    for key, val in keywords.items():
        if key in vendor.lower():
            category = val
            break

    return {
        "vendor": vendor,
        "date": date,
        "amount": amount,
        "category": category,
        "raw_text": text
    }