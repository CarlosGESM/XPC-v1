from pydantic import BaseModel
from datetime import datetime
from typing import List


class Abonado(BaseModel):
    id: int
    identificacion: str
    nombre: str
    estado: int


class Excepcion(BaseModel):
    id: int
    estado: int
    fecha_evento: datetime
    motivos: List[int]
    mids: List[int]
    sids: List[int]
    uids: List[int]
    abonados: List[int]
    licencias: List[int]
    cantidad_eventos: int
    fecha_registro: datetime


class Archivo(BaseModel):
    id: int
    excepciones: List[int]
    nombre: str
    path: str
    url: str
    estado: int
    fecha_registro: datetime

    class Config:
        orm_mode = True


class Mid(BaseModel):
    id: int
    descripcion: str


class Sid(BaseModel):
    id: int
    descripcion: str

    class Config:
        orm_mode = True
    

class Uid(BaseModel):
    id: int
    descripcion: str

    class Config:
        orm_mode = True
    

class Motivo(BaseModel):
    id: int
    descripcion: str

    class Config:
        orm_mode = True


class Licencia(BaseModel):
    id: int
    identificacion: str

    class Config:
        orm_mode = True
    
    
