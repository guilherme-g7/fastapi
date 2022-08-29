from typing import List, Any

from .aluno_curso_semestre_disciplina_nota_model import AlunoCursoSemestreDisciplinaNotaModel
from sqlalchemy.orm import Session

from .aluno_curso_semestre_disciplina_nota_schema import AlunoCursoSemestreDisciplinaNotaCreate

aluCurSemDisNotaModel = AlunoCursoSemestreDisciplinaNotaModel


def create_alu_cur_sem_dis_nota(db: Session, alu_cur_sem_dis_notas: AlunoCursoSemestreDisciplinaNotaCreate):
    novo_alu_cur_sem_dis_nota = AlunoCursoSemestreDisciplinaNotaModel(**alu_cur_sem_dis_notas.dict())
    db.add(novo_alu_cur_sem_dis_nota)
    db.commit()
    db.refresh(novo_alu_cur_sem_dis_nota)

    return novo_alu_cur_sem_dis_nota


def find_all_alu_cur_sem_dis_notas(db: Session) -> List[Any]:
    return db.query(aluCurSemDisNotaModel).all()


def find_one_alu_cur_sem_dis_nota(db: Session, alu_cur_sem_dis_nota_id: int):
    return db.query(aluCurSemDisNotaModel).filter(aluCurSemDisNotaModel.id == alu_cur_sem_dis_nota_id).first()
