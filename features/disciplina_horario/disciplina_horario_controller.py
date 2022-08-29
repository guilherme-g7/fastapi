from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .disciplina_horario_crud import(
    create_dis_horario,
    find_one_dis_horario,
    find_all_dis_horarios
)

from .disciplina_horario_schema import DisciplinaHorarioCreate

router = APIRouter()


@router.get("/disciplinas_horarios", status_code=status.HTTP_200_OK)
def get_all_disciplinas(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_dis_horarios(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe horários cadastrados!",
    )


@router.post("/new_disciplina_horario", status_code=status.HTTP_201_CREATED)
def post_dis_horario(disciplina_horario: DisciplinaHorarioCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_dis_horario(db, disciplina_horario):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
