from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .calendario_academico_crud import(
    create_calendario_academico,
    find_all_calendario_academico,
    find_one_calendario_academico
)

from .calendario_academico_schema import CalendarioAcademicoCreate

router = APIRouter()


@router.get("/calendarios_academicos", status_code=status.HTTP_200_OK)
def get_all_calendario_academico(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_calendario_academico(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe calendários acadêmicos cadastrados!",
    )


@router.post("/new_calendario_academico", status_code=status.HTTP_201_CREATED)
def post_calendario_academico(calendario_academico: CalendarioAcademicoCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_calendario_academico(db, calendario_academico):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
