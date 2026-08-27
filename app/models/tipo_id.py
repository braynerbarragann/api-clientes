from sqlalchemy import Column, Integer, String
from app.database.database import Base

class TipoId(Base):
    __tablename__ = "tipo_id"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))

