from typing import List, Any

from .instituicao_model import Instituicao, InstituicaoModel, InstituicaoCreate
from sqlalchemy.orm import Session

instituicaoModel = InstituicaoModel


def create_instituicao(db: Session, instituicao: InstituicaoCreate):
    nova_inst = InstituicaoModel(**instituicao.dict())
    db.add(nova_inst)
    db.commit()
    db.refresh(nova_inst)

    return nova_inst


def find_all_instituicao(db: Session):
    return db.query(instituicaoModel).all()


def find_one_instituicao(db: Session, instituicao_id: int):
    return db.query(instituicaoModel).filter(instituicaoModel.id == instituicao_id).first()
