from typing import List, Any

from .campus_model import Campus, CampusCreate, CampusModel
from sqlalchemy.orm import Session


campusModel = CampusModel()


def create_campus(db: Session, campus: CampusCreate):
    novo_campus = CampusModel(**campus.dict())
    db.add(novo_campus)
    db.commit()
    db.refresh(novo_campus)

    return novo_campus


def find_all_campus(db: Session) -> List[Any]:
    return db.query(campusModel).all()


def find_one_campus(db: Session, campus_id: int):
    return db.query(campusModel).filter(campusModel.id == campus_id).first()
