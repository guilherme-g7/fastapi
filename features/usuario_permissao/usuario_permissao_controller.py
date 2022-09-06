from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .usuario_permissao_crud import(
    create_usuario_permissao,
    find_all_usuarios_permissoes,
    find_one_usuario_permissao
)

from .usuario_permissao_schema import UsuarioPermissaoCreate

router = APIRouter()


@router.get("/usuarios_permissoes", status_code=status.HTTP_200_OK)
def get_all_usuarios_permissoes(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_usuarios_permissoes(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe usuários cadastrados!",
    )


@router.post("/new_usuario_permissao", status_code=status.HTTP_201_CREATED)
def post_usuario_permissao(usuario_permissao: UsuarioPermissaoCreate, db: Session = Depends(get_db),
                 ) -> Dict[str, Union[float, int, str]]:
    if result := create_usuario_permissao(db, usuario_permissao):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
