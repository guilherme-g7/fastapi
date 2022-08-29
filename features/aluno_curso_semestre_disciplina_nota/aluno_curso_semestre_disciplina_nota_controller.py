from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .aluno_curso_semestre_disciplina_nota_crud import(
    create_alu_cur_sem_dis_nota,
    find_all_alu_cur_sem_dis_notas,
    find_one_alu_cur_sem_dis_nota
)

from .aluno_curso_semestre_disciplina_nota_schema import AlunoCursoSemestreDisciplinaNotaCreate

router = APIRouter()


@router.get("/alunos_cursos_semestres_disciplinas_notas", status_code=status.HTTP_200_OK)
def get_all_alu_cur_sem_dis_notas(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_alu_cur_sem_dis_notas(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe notas cadastrados!",
    )


@router.post("/new_alu_cur_sem_dis_nota", status_code=status.HTTP_201_CREATED)
def post_alu_cur_sem_dis_nota(alu_cur_sem_dis_nota: AlunoCursoSemestreDisciplinaNotaCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_alu_cur_sem_dis_nota(db, alu_cur_sem_dis_nota):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )