from typing import List, Any

from .disciplina_professor_model import DisciplinaProfessorModel
from sqlalchemy.orm import Session

from .disciplina_professor_schema import DisciplinaProfessorCreate

disciplinaProfessorModel = DisciplinaProfessorModel


def create_dis_professor(db: Session, disciplina_professor: DisciplinaProfessorCreate):
    novo_dis_horario = DisciplinaProfessorModel(**disciplina_professor.dict())
    db.add(novo_dis_horario)
    db.commit()
    db.refresh(novo_dis_horario)

    return novo_dis_horario


def find_all_dis_horarios(db: Session) -> List[Any]:
    return db.query(disciplinaProfessorModel).all()


def find_one_dis_horario(db: Session, dis_professor_id: int):
    return db.query(disciplinaProfessorModel).filter(disciplinaProfessorModel.id == dis_professor_id).first()
