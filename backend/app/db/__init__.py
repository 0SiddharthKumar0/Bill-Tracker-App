from app.db.database import engine, Base
from app.models import Receipt

print("Creating tables...")
Base.metadata.create_all(engine)
print("Done.")