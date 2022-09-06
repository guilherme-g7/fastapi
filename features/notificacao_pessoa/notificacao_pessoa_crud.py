from typing import List, Any

from .notificacao_pessoa_model import NotificacaoPessoaModel
from sqlalchemy.orm import Session

from .notificacao_pessoa_schema import NotificacaoPessoaCreate

notificacaoPessoaModel = NotificacaoPessoaModel


def create_notificacao_pessoa(db: Session, notificacao_pessoa: NotificacaoPessoaCreate):
    nova_notificacao_pessoa = NotificacaoPessoaModel(**notificacao_pessoa.dict())
    db.add(nova_notificacao_pessoa)
    db.commit()
    db.refresh(nova_notificacao_pessoa)

    return nova_notificacao_pessoa


def find_all_notificacoes_pessoas(db: Session) -> List[Any]:
    return db.query(notificacaoPessoaModel).all()


def find_one_notificacao_pessoa(db: Session, notificacao_pessoa_id: int):
    return db.query(notificacaoPessoaModel).filter(notificacaoPessoaModel.id == notificacao_pessoa_id).first()
