from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .curso_crud import(
    create_curso,
    find_all_curso,
    find_one_curso
)

from .curso_schema import CursoCreate

router = APIRouter()


@router.get("/cursos", status_code=status.HTTP_200_OK)
def get_all_campus(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_curso(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe cursos cadastrados!",
    )


@router.post("/new_curso", status_code=status.HTTP_201_CREATED)
def post_campus(curso: CursoCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_curso(db, curso):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
