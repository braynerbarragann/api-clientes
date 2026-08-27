from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base



database_config = {
    "user": "root",
    "password": "admin123",
    "host":"localhost",
    "port": 3306,
    "database": "clientes"
}

DATABASE_URL = (
    f"mysql+pymysql://{database_config['user']}:{database_config['password']}"
    f"@{database_config['host']}:{database_config['port']}"
    f"/{database_config['database']}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()   