from typing import List, Any

from .permissao_model import PermissaoModel
from sqlalchemy.orm import Session

from .permissao_schema import PermissaoCreate

permissaoModel = PermissaoModel


def create_permissao(db: Session, permissao: PermissaoCreate):
    nova_permissao = PermissaoModel(**permissao.dict())
    db.add(nova_permissao)
    db.commit()
    db.refresh(nova_permissao)

    return nova_permissao


def find_all_permissao(db: Session) -> List[Any]:
    return db.query(permissaoModel).all()


def find_one_permissao(db: Session, permissao_id: int):
    return db.query(permissaoModel).filter(permissaoModel.id == permissao_id).first()
