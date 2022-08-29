from typing import List, Any

from .usuario_model import UsuarioModel
from sqlalchemy.orm import Session

from .usuario_schema import UsuarioCreate

usuarioModel = UsuarioModel


def create_usuario(db: Session, usuario: UsuarioCreate):
    novo_usuario = UsuarioModel(**usuario.dict())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


def find_all_usuario(db: Session) -> List[Any]:
    return db.query(usuarioModel).all()


def find_one_usuario(db: Session, usuario_id: int):
    return db.query(usuarioModel).filter(usuarioModel.id == usuario_id).first()
