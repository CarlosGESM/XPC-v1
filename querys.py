from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_exception(
    db: Session, data: dict, mid: schemas.Mid, sid: schemas.Mid,
    uid: schemas.Uid, motivo: schemas.Motivo, licencia: schemas.Licencia,
    abonado: schemas.Abonado
):
    db_exception = models.Excepcion(
        estado=data['estado'],
        fecha_evento=data['fecha_evento'],
        mids=list[mid.id],
        sids=[sid.id],
        uids=[uid.id],
        motivos=[motivo.id],
        licencias=[licencia.id],
        abonados=[abonado.id],
        cantidad_eventos=data['cantidad_eventos'],
        fecha_registro=data['fecha_registro']
    )
    db.add(db_exception)
    db.commit()
    db.refresh(db_exception)
    return db_exception


def get_exceptions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Excepcion).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item