# Receipt & Bill Tracker App

A full-stack application designed to upload, extract, parse, and store receipt or bill data using Optical Character Recognition (OCR) and pattern matching, presented in a user-friendly web interface.

---

## ✨ Features

* Upload receipts in PDF format
* Extract raw text using OCR
* Parse key fields like date, vendor, total amount, and items
* Store parsed data in a SQLite database
* View analytics (list of receipts with summaries)
* Modular and clean architecture

---

## 🔧 Technologies Used

### Frontend:

* **React + Vite**: Modern web UI
* **Tailwind CSS**: Utility-first responsive design
* **Axios**: HTTP client for API interaction

### Backend:

* **FastAPI**: High-performance Python API framework
* **SQLModel**: ORM based on SQLAlchemy + Pydantic
* **SQLite**: Lightweight embedded database
* **PyMuPDF**: PDF text extraction (OCR-compatible)
* **Regex**: For field-level parsing
* **Poppler (via MuPDF)**: Backend OCR support for PDFs

---

## 📁 Folder Structure

```
Bill Tracker App
├── backend
│   ├── app
│   │   ├── api
│   │   │   ├── analytics.py
│   │   │   └── upload.py
│   │   ├── crud.py
│   │   ├── db
│   │   │   ├── __init__.py
│   │   │   ├── database.py
│   │   │   └── models.py
│   │   ├── main.py
│   │   ├── services
│   │   │   ├── ocr.py
│   │   │   └── parser.py
│   │   └── utils.py
│   ├── venv
│   └── requirements.txt
├── bill-tracker-app (frontend)
│   ├── src
│   │   ├── api.js
│   │   ├── App.jsx
│   │   ├── components
│   │   └── index.css
│   └── vite.config.js
└── README.md
```

---

## ⚡ Setup Instructions

### Prerequisites

* Python 3.11+
* Node.js + npm
* Poppler (PDF OCR)

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt

# Add Poppler to PATH
setx PATH "%PATH%;C:\\Program Files\\poppler-24.02.0\\Library\\bin"

# Set PYTHONPATH
$env:PYTHONPATH = "$PWD"

# Initialize DB
python -m app.db.init_db

# Run server
uvicorn app.main:app --reload
```

### Frontend

```bash
cd bill-tracker-app
npm install
npm run dev
```

---

## 🔎 API Reference

### `POST /upload/`

Uploads a receipt PDF and stores parsed fields.

### `GET /analytics/`

Returns a list of stored receipts and summary data.

---

## 📊 Core Modules

### `ocr.py`

Uses PyMuPDF to extract raw text from PDFs. Configured with Poppler.

### `parser.py`

Uses regex patterns to identify:

* Vendor name
* Transaction date
* Total amount
* Itemized details (WIP/improvable)

### `crud.py`

CRUD logic using SQLModel ORM.

### `utils.py`

File validation: PDF, size check, etc.

---

## 🛡️ Error Handling

* 422 error if parsing fails
* 400 for invalid file types
* Global exception handling via FastAPI

---

## 🚀 Roadmap

* [x] Basic upload + parse
* [x] OCR integration
* [x] UI analytics
* [ ] Export to CSV
* [ ] Multi-page receipt support
* [ ] Upload via image (JPG, PNG)
* [ ] Real-time parsing progress
* [ ] User auth + multi-tenancy

---

## 🔢 Performance Notes

* Handles single-page PDFs within \~1 sec parse time
* SQLite used for simplicity; can switch to PostgreSQL
* Scalable FastAPI + React stack

---

## 📤 Deployment

* Use Docker for both backend and frontend
* Use Gunicorn + Nginx for production
* CI/CD via GitHub Actions (optional)

---

## 📸 Screenshots

Add demo screenshots or gif walkthroughs here.

---

## ✉️ Feedback & Contribution

Open to feature requests or PRs. Raise an issue or fork the repo.

---

## © License

MIT License

---

## 👤 Author

**Siddharth Kumar**
MTech Project – 2025

---

Ready to use. Ready to extend. Built for clarity and speed.

---
