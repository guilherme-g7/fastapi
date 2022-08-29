from typing import Any, List, Dict, Union

from starlette import status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from fastapi.param_functions import Depends
from fastapi.exceptions import HTTPException


from db.database import get_db

from .disciplina_professor_crud import(
    create_dis_professor,
    find_all_dis_horarios,
    find_one_dis_horario
)

from .disciplina_professor_schema import DisciplinaProfessorCreate

router = APIRouter()


@router.get("/disciplinas_professores", status_code=status.HTTP_200_OK)
def get_all_disciplinas(db: Session = Depends(get_db)) -> List[Any]:
    if result := find_all_dis_horarios(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Não existe disciplinas professores cadastrados!",
    )


@router.post("/new_disciplina_professor", status_code=status.HTTP_201_CREATED)
def post_dis_professor(disciplina_professor: DisciplinaProfessorCreate, db: Session = Depends(get_db),
                ) -> Dict[str, Union[float, int, str]]:
    if result := create_dis_professor(db, disciplina_professor):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )
