from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nombre: str
    mail: str
    telefono: str
    tipo_id: int
    genero_id: int



class ClienteResponse(BaseModel):
    id: int
    nombre: str
    mail: str
    telefono: str
    tipo_id: int
    genero_id: int

    model_config = {
        "from_attributes": True
    }

