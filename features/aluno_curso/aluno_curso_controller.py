from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .aluno_curso_crud import(
    create_aluno_curso,
    find_all_aluno_curso,
    find_one_aluno_curso
)

from .aluno_curso_schema import AlunoCursoCreate

router = APIRouter()


@router.get("/alunos_cursos", status_code=status.HTTP_200_OK)
def get_all_aluno_curso(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_aluno_curso(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe campus cadastrados!",
    )


@router.post("/new_aluno_curso", status_code=status.HTTP_201_CREATED)
def post_aluno_curso(aluno_curso: AlunoCursoCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_aluno_curso(db, aluno_curso):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )