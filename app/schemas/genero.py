from pydantic import BaseModel

class GeneroCreate(BaseModel):
    nombre: str

class GeneroResponse(BaseModel):
    
    nombre: str

    model_config = {
        "from_attributes": True
    }