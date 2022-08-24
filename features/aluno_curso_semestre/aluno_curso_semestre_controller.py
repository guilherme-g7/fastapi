from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .aluno_curso_semestre_crud import(
    create_aluno_curso_semestre,
    find_all_aluno_curso_semestre,
    find_one_aluno_curso_semestre
)

from .aluno_curso_semestre_schema import AlunoCursoSemestreCreate

router = APIRouter()


@router.get("/alunos_cursos_semestres", status_code=status.HTTP_200_OK)
def get_all_aluno_curso_semestres(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_aluno_curso_semestre(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe campus cadastrados!",
    )


@router.post("/new_aluno_curso_semestre", status_code=status.HTTP_201_CREATED)
def post_campus(aluno_curso_semestre: AlunoCursoSemestreCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_aluno_curso_semestre(db, aluno_curso_semestre):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )