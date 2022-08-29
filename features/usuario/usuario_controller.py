from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .usuario_crud import(
    create_usuario,
    find_all_usuario,
    find_one_usuario
)

from .usuario_schema import UsuarioCreate

router = APIRouter()


@router.get("/usuarios", status_code=status.HTTP_200_OK)
def get_all_usuarios(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_usuario(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe usuários cadastrados!",
    )


@router.post("/new_usuario", status_code=status.HTTP_201_CREATED)
def post_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_usuario(db, usuario):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
