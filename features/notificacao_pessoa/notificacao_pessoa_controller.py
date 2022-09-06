from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .notificacao_pessoa_crud import(
    create_notificacao_pessoa,
    find_all_notificacoes_pessoas,
    find_one_notificacao_pessoa
)

from .notificacao_pessoa_schema import NotificacaoPessoaCreate

router = APIRouter()


@router.get("/notificacoes_pessoas", status_code=status.HTTP_200_OK)
def get_all_notificacoes_pessoas(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_notificacoes_pessoas(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe notificações pessoas cadastradas!",
    )


@router.post("/new_notificacao_pessoa", status_code=status.HTTP_201_CREATED)
def post_notificacao_pessoa(notificacao_pessoa: NotificacaoPessoaCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_notificacao_pessoa(db, notificacao_pessoa):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
