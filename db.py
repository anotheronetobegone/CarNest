import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

load_dotenv(".env.development")

DB_TYPE = os.getenv("DB_TYPE")

if DB_TYPE == "sqlite":
    DATABASE_URL = f"sqlite:///{os.getenv('DB_PATH')}"

else:
    DATABASE_URL = (
        f"mysql+pymysql://"
        f"{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

def get_db():
    """
    Fetches DB
    """
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()