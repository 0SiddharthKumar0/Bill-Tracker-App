from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import upload, analytics

app = FastAPI(title="Receipt Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, whitelist your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])

@app.get("/")
def root():
    return {"message": "Receipt Tracker API is running."}