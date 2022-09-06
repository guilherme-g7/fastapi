from typing import List, Any

from .usuario_permissao_model import UsuarioPermissaoModel
from sqlalchemy.orm import Session

from .usuario_permissao_schema import UsuarioPermissaoCreate

usuarioPermissaoModel = UsuarioPermissaoModel


def create_usuario_permissao(db: Session, usuario_permissao: UsuarioPermissaoCreate):
    novo_usuario_permissao = UsuarioPermissaoModel(**usuario_permissao.dict())
    db.add(novo_usuario_permissao)
    db.commit()
    db.refresh(novo_usuario_permissao)

    return novo_usuario_permissao


def find_all_usuarios_permissoes(db: Session) -> List[Any]:
    return db.query(usuarioPermissaoModel).all()


def find_one_usuario_permissao(db: Session, usuario_permissao_id: int):
    return db.query(usuarioPermissaoModel).filter(usuarioPermissaoModel.id == usuario_permissao_id).first()
