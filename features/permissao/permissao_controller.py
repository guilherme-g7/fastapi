from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .permissao_crud import(
    create_permissao,
    find_all_permissao,
    find_one_permissao
)

from .permissao_schema import PermissaoCreate

router = APIRouter()


@router.get("/permissoes", status_code=status.HTTP_200_OK)
def get_all_permissoes(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_permissao(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe permissões cadastradas!",
    )


@router.post("/new_permissao", status_code=status.HTTP_201_CREATED)
def post_permissao(permissao: PermissaoCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_permissao(db, permissao):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
