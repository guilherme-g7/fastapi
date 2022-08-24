from typing import List, Any

from .aluno_curso_semestre_disciplina_model import AlunoCursoSemestreDisciplinaModel
from sqlalchemy.orm import Session

from .aluno_curso_semestre_disciplina_schema import AlunoCursoSemestreDisciplinaCreate

alunoCursoSemDisciplinaModel = AlunoCursoSemestreDisciplinaModel


def create_aluno_curso_semestre_disciplina(db: Session, aluno_curso_semestre_discip: AlunoCursoSemestreDisciplinaCreate):
    novo_aluno_curso_semestre_disciplina = AlunoCursoSemestreDisciplinaModel(**aluno_curso_semestre_discip.dict())
    db.add(novo_aluno_curso_semestre_disciplina)
    db.commit()
    db.refresh(novo_aluno_curso_semestre_disciplina)

    return novo_aluno_curso_semestre_disciplina


def find_all_aluno_curso_semestre_disciplina(db: Session) -> List[Any]:
    return db.query(alunoCursoSemDisciplinaModel).all()


def find_one_aluno_curso_semestre_disciplina(db: Session, aluno_curso_semestre_disciplina_id: int):
    return db.query(alunoCursoSemDisciplinaModel).filter(alunoCursoSemDisciplinaModel.id == aluno_curso_semestre_disciplina_id).first()
