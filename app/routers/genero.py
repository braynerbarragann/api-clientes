from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.genero import Genero
from app.schemas.genero import GeneroCreate, GeneroResponse
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/generos", response_model=list[GeneroResponse])
def obtener_generos(db: Session = Depends(get_db)):
    return db.query(Genero).all()

@router.post("/generos", response_model=GeneroCreate)
def crear_genero(
    genero: GeneroCreate,
    db: Session = Depends(get_db)
):
    nuevo_genero = Genero(
        nombre=genero.nombre
    )

    db.add(nuevo_genero)
    db.commit()
    db.refresh(nuevo_genero)

    return nuevo_genero