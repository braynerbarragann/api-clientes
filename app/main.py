from fastapi import FastAPI
from app.database.database import Base, engine
from app.models.cliente import Cliente
from app.models.genero import Genero
from app.models.tipo_id import TipoId
from app.routers import tipo_id
from app.routers import cliente
from app.routers import genero


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}

app.include_router(cliente.router)
app.include_router(genero.router)
app.include_router(tipo_id.router)