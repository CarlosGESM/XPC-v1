from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class Abonado(Base):
    __tablename__ = "abonados"

    id = Column(Integer, primary_key=True, index=True)
    identificacion = Column(String, unique=True, index=True)
    nombre = Column(String, default=True)
    estado = Column(Integer, default=True)

    excepciones = relationship("Excepcion", back_populates="abonados")


class Excepcion(Base):
    __tablename__ = "excepciones"

    # attributes
    id = Column(Integer, primary_key=True, index=True)
    estado = Column(Integer, index=True)
    fecha_evento = Column(Date)
    mid_id = Column(Integer, ForeignKey("mids.id"))
    sid_id = Column(Integer, ForeignKey("sids.id"))
    uid_id = Column(Integer, ForeignKey("uids.id"))
    motivo_id = Column(Integer, ForeignKey("motivos.id"))
    licencia_id = Column(Integer, ForeignKey("licencias.id"))
    abonado_id = Column(Integer, ForeignKey("abonados.id"))
    cantidad_eventos = Column(Integer)
    fecha_registro = Column(Date)


    #references
    mids = relationship("Mid", back_populates="excepciones")
    sids = relationship("Sid", back_populates="excepciones")
    uids = relationship("Uid", back_populates="excepciones")
    motivos = relationship("Motivo", back_populates="excepciones")
    licencias = relationship("Licencia", back_populates="excepciones")
    abonados = relationship("Abonado", back_populates="excepciones")


class Archivo(Base):
    __tablename__ = "archivos"

    id = Column(Integer, primary_key=True, index=True)
    exception_id = Column(Integer, index=True)
    nombre = Column(String, index=True)
    estado = Column(Integer, index=True)
    fecha_registro = Column(Date, index=True)



class Mid(Base):
    __tablename__ = "mids"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True)

    excepciones = relationship("Exception", back_populates="mids")


class Sid(Base):
    __tablename__ = "sids"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True)

    excepciones = relationship("Exception", back_populates="sids")


class Uid(Base):
    __tablename__ = "uids"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True)

    excepciones = relationship("Exception", back_populates="uids")


class Motivo(Base):
    __tablename__ = "motivos"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True)

    excepciones = relationship("Exception", back_populates="motivos")


class Licencia(Base):
    __tablename__ = "licencias"

    id = Column(Integer, primary_key=True, index=True)
    identificacion = Column(String, index=True)

    excepciones = relationship("Exception", back_populates="licencias")