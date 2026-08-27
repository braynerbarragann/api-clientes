from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    mail = Column(String(50), nullable=False)
    telefono = Column(String(50), nullable=False)

    tipo_id = Column(Integer, ForeignKey("tipo_id.id"), nullable=False)
    genero_id = Column(Integer, ForeignKey("genero.id"), nullable=False)