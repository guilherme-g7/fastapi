from typing import List, Any

from .calendario_academico_model import CalendarioAcademicoModel
from sqlalchemy.orm import Session

from .calendario_academico_schema import CalendarioAcademicoCreate

calendarioAacademicoModel = CalendarioAcademicoModel


def create_calendario_academico(db: Session, calendario_academico: CalendarioAcademicoCreate):
    novo_calendario = CalendarioAcademicoModel(**calendario_academico.dict())
    db.add(novo_calendario)
    db.commit()
    db.refresh(novo_calendario)

    return novo_calendario


def find_all_calendario_academico(db: Session) -> List[Any]:
    return db.query(calendarioAacademicoModel).all()


def find_one_calendario_academico(db: Session, calendario_academico_id: int):
    return db.query(calendarioAacademicoModel).filter(calendarioAacademicoModel.id == calendario_academico_id).first()
