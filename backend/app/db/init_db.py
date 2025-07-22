from sqlalchemy.orm import Session
from app.db.database import engine, Base

def init_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Done.")

if __name__ == "__main__":
    init_db()