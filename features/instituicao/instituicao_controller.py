from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .instituicao_crud import (
    create_instituicao,
    find_all_instituicao,
    find_one_instituicao
)

from .instituicao_model import InstituicaoCreate, Instituicao

router = APIRouter()


@router.get("/instituicoes", status_code=status.HTTP_200_OK, response_model=list[Instituicao])
def get_all_instituicao(db: Session = Depends(get_db)):
    if result := find_all_instituicao(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe instituições cadastradas!",
    )


@router.post("/new_instituicao", status_code=status.HTTP_201_CREATED)
def post_instituicao(instituicao: InstituicaoCreate, db: Session = Depends(get_db),
                     ) -> Dict[str, Union[float, int, str]]:
    if result := create_instituicao(db, instituicao):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
