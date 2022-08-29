from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException

from db.database import get_db

from .notificacao_crud import (
    create_notificacao,
    find_all_notificacao,
    find_one_notificacao
)

from .notificacao_schema import NotificacaoCreate

router = APIRouter()


@router.get("/notificacoes", status_code=status.HTTP_200_OK)
def get_all_notificacoes(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_notificacao(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe notificações cadastradas!",
    )


@router.post("/new_notificacao", status_code=status.HTTP_201_CREATED)
def post_notificacao(notificacao: NotificacaoCreate, db: Session = Depends(get_db),
                     ) -> Dict[str, Union[float, int, str]]:
    if result := create_notificacao(db, notificacao):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
