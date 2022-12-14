from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .aluno_curso_semestre_disciplina_crud import(
    create_aluno_curso_semestre_disciplina,
    find_all_aluno_curso_semestre_disciplina,
    find_one_aluno_curso_semestre_disciplina
)

from .aluno_curso_semestre_disciplina_schema import AlunoCursoSemestreDisciplinaCreate

router = APIRouter()


@router.get("/alunos_cursos_semestres_disciplinas", status_code=status.HTTP_200_OK)
def get_all_aluno_curso_semestres_discip(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_aluno_curso_semestre_disciplina(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe campus cadastrados!",
    )


@router.post("/new_alu_cur_sem_discip", status_code=status.HTTP_201_CREATED)
def post_alu_cur_sem_discip(aluno_curso_semestre_discip: AlunoCursoSemestreDisciplinaCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_aluno_curso_semestre_disciplina(db, aluno_curso_semestre_discip):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )