from typing import List, Any

from .aluno_curso_model import AlunoCursoModel
from sqlalchemy.orm import Session

from .aluno_curso_schema import AlunoCursoCreate

alunoCursoModel = AlunoCursoModel


def create_aluno_curso(db: Session, aluno_curso: AlunoCursoCreate):
    novo_aluno_curso = AlunoCursoModel(**aluno_curso.dict())
    db.add(novo_aluno_curso)
    db.commit()
    db.refresh(novo_aluno_curso)

    return novo_aluno_curso


def find_all_aluno_curso(db: Session) -> List[Any]:
    return db.query(alunoCursoModel).all()


def find_one_aluno_curso(db: Session, aluno_curso_id: int):
    return db.query(alunoCursoModel).filter(alunoCursoModel.id == aluno_curso_id).first()
