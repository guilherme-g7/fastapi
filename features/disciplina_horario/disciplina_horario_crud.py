from typing import List, Any

from .disciplina_horario_model import DisciplinaHorarioModel
from sqlalchemy.orm import Session

from .disciplina_horario_schema import DisciplinaHorarioCreate

disciplinaHorarioModel = DisciplinaHorarioModel


def create_dis_horario(db: Session, disciplina_horario: DisciplinaHorarioCreate):
    novo_dis_horario = DisciplinaHorarioModel(**disciplina_horario.dict())
    db.add(novo_dis_horario)
    db.commit()
    db.refresh(novo_dis_horario)

    return novo_dis_horario


def find_all_dis_professores(db: Session) -> List[Any]:
    return db.query(disciplinaHorarioModel).all()


def find_one_dis_professor(db: Session, dis_horario_id: int):
    return db.query(disciplinaHorarioModel).filter(disciplinaHorarioModel.id == dis_horario_id).first()
