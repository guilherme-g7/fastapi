from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .notificacao_pessoa_config_crud import(
    create_notificacao_pessoa_config,
    find_all_notificacoes_pessoas_configs,
    find_one_notificacao_pessoa_config
)

from .notificacao_pessoa_config_schema import NotificacaoPessoaConfigCreate

router = APIRouter()


@router.get("/notificacoes_pessoas_configs", status_code=status.HTTP_200_OK)
def get_all_notificacoes_pessoas_configs(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_notificacoes_pessoas_configs(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe notificações pessoas configurações cadastradas!",
    )


@router.post("/new_notificacao_pessoa_config", status_code=status.HTTP_201_CREATED)
def post_notificacao_pessoa_config(notificacao_pessoa_config: NotificacaoPessoaConfigCreate, db: Session = Depends(get_db),
                                   ) -> Dict[str, Union[float, int, str]]:
    if result := create_notificacao_pessoa_config(db, notificacao_pessoa_config):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
