from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .pessoa_crud import(
    create_pessoa,
    find_all_pessoa,
    find_one_pessoa
)

from .pessoa_schema import PessoaCreate

router = APIRouter()


@router.get("/pessoas", status_code=status.HTTP_200_OK)
def get_all_campus(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_pessoa(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe cursos cadastrados!",
    )


@router.post("/new_pessoa", status_code=status.HTTP_201_CREATED)
def post_campus(curso: PessoaCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_pessoa(db, curso):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
