from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate, ClienteResponse
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/clientes", response_model=list[ClienteResponse])
def obtener_clientes(db: Session = Depends(get_db)):
    return db.query(Cliente).all()

@router.get("/clientes/{cliente_id}",  response_model=ClienteResponse)
def obtener_cliente(cliente_id: int, db: Session = Depends(get_db)):

    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    return cliente

@router.post("/clientes", response_model=ClienteResponse)
def crear_cliente(
    cliente: ClienteCreate,
    db: Session = Depends(get_db)
):
    #print("ENTRÉ AL POST")
    nuevo_cliente = Cliente(
        nombre=cliente.nombre,
        mail=cliente.mail,  
        telefono=cliente.telefono,
        tipo_id=cliente.tipo_id,
        genero_id=cliente.genero_id
    )

    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)

    #print(type(nuevo_cliente))
    #print(nuevo_cliente)

    return nuevo_cliente


@router.put("/clientes/{cliente_id}", response_model=ClienteResponse)
def editar_cliente(
    cliente_id: int,
    cliente: ClienteCreate,
    db: Session = Depends(get_db)
):
    cliente_db = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if cliente_db is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    cliente_db.nombre = cliente.nombre
    cliente_db.mail = cliente.mail
    cliente_db.telefono = cliente.telefono
    cliente_db.tipo_id = cliente.tipo_id
    cliente_db.genero_id = cliente.genero_id

    db.commit()
    db.refresh(cliente_db)

    return cliente_db


@router.delete("/clientes/{cliente_id}")
def eliminar_cliente( cliente_id: int,db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    
    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    db.delete(cliente)
    db.commit()

    return {"mensaje": "Cliente eliminado correctamente"}