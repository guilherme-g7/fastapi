from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException

from db.database import get_db
from features.carga_inicial.carga_inicial_crud import create_carga_inicial

router = APIRouter()


@router.post("/carga_inicial", status_code=status.HTTP_201_CREATED)
async def carga_inicial(json: Dict[str, Union[float, int, str]], db: Session = Depends(get_db)) -> Dict[
    str, Union[float, int, str]]:
    print(json)
    if result := create_carga_inicial(json, db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
