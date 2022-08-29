from typing import List, Any

from .disciplina_model import DisciplinaModel
from sqlalchemy.orm import Session

from .disciplina_schema import DisciplinaCreate

disciplinaModel = DisciplinaModel


def create_disciplina(db: Session, disciplina: DisciplinaCreate):
    novo_disciplina = DisciplinaModel(**disciplina.dict())
    db.add(novo_disciplina)
    db.commit()
    db.refresh(novo_disciplina)

    return novo_disciplina


def find_all_disciplina(db: Session) -> List[Any]:
    return db.query(disciplinaModel).all()


def find_one_disciplina(db: Session, disciplina_id: int):
    return db.query(disciplinaModel).filter(disciplinaModel.id == disciplina_id).first()
