from pydantic import BaseModel

# Modelo para el historial de accidentes
class Accidente(BaseModel):
    id: int
    vehiculo_id: int
    fecha: str
    descripcion: str


# Modelo para el historial de robos
class Robo(BaseModel):
    id: int
    vehiculo_id: int
    fecha: str
    descripcion: str


# Modelo para el historial de papeletas
class Papeleta(BaseModel):
    id: int
    vehiculo_id: int
    fecha: str
    descripcion: str


# Modelo para el historial de deudas
class Deuda(BaseModel):
    id: int
    vehiculo_id: int
    monto: float
    descripcion: str