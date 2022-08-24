from typing import List, Any

from .aluno_curso_semestre_model import AlunoCursoSemestreModel
from sqlalchemy.orm import Session

from .aluno_curso_semestre_schema import AlunoCursoSemestreCreate

alunoCursoSemestreModel = AlunoCursoSemestreModel


def create_aluno_curso_semestre(db: Session, aluno_curso_semestre: AlunoCursoSemestreCreate):
    novo_aluno_curso_semestre = AlunoCursoSemestreModel(**aluno_curso_semestre.dict())
    db.add(novo_aluno_curso_semestre)
    db.commit()
    db.refresh(novo_aluno_curso_semestre)

    return novo_aluno_curso_semestre


def find_all_aluno_curso_semestre(db: Session) -> List[Any]:
    return db.query(alunoCursoSemestreModel).all()


def find_one_aluno_curso_semestre(db: Session, aluno_curso_semestre_id: int):
    return db.query(alunoCursoSemestreModel).filter(alunoCursoSemestreModel.id == aluno_curso_semestre_id).first()
