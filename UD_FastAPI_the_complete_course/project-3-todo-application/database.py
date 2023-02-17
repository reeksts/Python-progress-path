from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Sqlite database connection:
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
# engine = create_engine(
#    SQLALCHEMY_DATABASE_URL,
#    connect_args={"check_same_thread": False}
# )

# Postgresql database connection
SQLALCHEMY_DATABASE_URL = (
    "postgresql://postgres:Ledusmaize1@localhost/TodoApplicationDatabase"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
