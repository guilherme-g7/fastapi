from typing import List, Any

from .curso_model import CursoModel
from sqlalchemy.orm import Session

from .curso_schema import CursoCreate

cursoModel = CursoModel


def create_curso(db: Session, curso: CursoCreate):
    novo_curso = CursoModel(**curso.dict())
    db.add(novo_curso)
    db.commit()
    db.refresh(novo_curso)

    return novo_curso


def find_all_curso(db: Session) -> List[Any]:
    return db.query(cursoModel).all()


def find_one_curso(db: Session, curso_id: int):
    return db.query(cursoModel).filter(cursoModel.id == curso_id).first()
