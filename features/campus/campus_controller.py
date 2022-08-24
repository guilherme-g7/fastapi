from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .campus_crud import(
    create_campus,
    find_all_campus,
    find_one_campus
)

from .campus_schema import CampusCreate

router = APIRouter()


@router.get("/campus", status_code=status.HTTP_200_OK)
def get_all_campus(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_campus(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe campus cadastrados!",
    )


@router.post("/new_campus", status_code=status.HTTP_201_CREATED)
def post_campus(campus: CampusCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_campus(db, campus):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )