from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./receipts.db"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    return Session(engine)

Base = SQLModel