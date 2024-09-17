from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite database
DATABASE_URL = "sqlite:///./users.db"

# Create SQLite engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Local session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Get DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
