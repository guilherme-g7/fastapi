from typing import List, Any

from .notificacao_model import NotificacaoModel
from sqlalchemy.orm import Session

from .notificacao_schema import NotificacaoCreate

notificacaoModel = NotificacaoModel


def create_notificacao(db: Session, notificacao: NotificacaoCreate):
    nova_notificacao = NotificacaoModel(**notificacao.dict())
    db.add(nova_notificacao)
    db.commit()
    db.refresh(nova_notificacao)

    return nova_notificacao


def find_all_notificacao(db: Session) -> List[Any]:
    return db.query(notificacaoModel).all()


def find_one_notificacao(db: Session, notificacao_id: int):
    return db.query(notificacaoModel).filter(notificacaoModel.id == notificacao_id).first()
