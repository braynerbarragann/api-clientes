from pydantic import BaseModel

class TipoIdCreate(BaseModel):
    nombre: str

class TipoIdCreateResponse(BaseModel):
    nombre: str
    model_config = {
        "from_attributes": True
    }