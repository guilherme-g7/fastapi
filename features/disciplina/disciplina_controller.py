from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .disciplina_crud import(
    create_disciplina,
    find_all_disciplina,
    find_one_disciplina
)

from .disciplina_schema import DisciplinaCreate

router = APIRouter()


@router.get("/disciplinas", status_code=status.HTTP_200_OK)
def get_all_disciplinas(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_disciplina(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe cursos cadastrados!",
    )


@router.post("/new_disciplina", status_code=status.HTTP_201_CREATED)
def post_disciplina(disciplina: DisciplinaCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_disciplina(db, disciplina):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
