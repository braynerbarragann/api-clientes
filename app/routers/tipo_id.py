from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.tipo_id import TipoId
from app.schemas.tipo_id import TipoIdCreate, TipoIdCreateResponse
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tipos_id", response_model=list[TipoIdCreateResponse])
def obtener_tipos_id(db: Session = Depends(get_db)):
    return db.query(TipoId).all()


@router.post("/tipos_id", response_model=TipoIdCreate)
def crear_tipo_id(
    tipo_id: TipoIdCreate,
    db: Session = Depends(get_db)
):
    nuevo_tipo_id = TipoId(
        nombre= tipo_id.nombre
    )

    db.add(nuevo_tipo_id)
    db.commit()
    db.refresh(nuevo_tipo_id)

    return nuevo_tipo_id