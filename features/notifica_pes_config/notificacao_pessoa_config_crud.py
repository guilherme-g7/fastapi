from typing import List, Any

from .notificacao_pessoa_config_model import NotificacaoPessoaConfigModel
from sqlalchemy.orm import Session

from .notificacao_pessoa_config_schema import NotificacaoPessoaConfigCreate

notificacaoPessoaConfigModel = NotificacaoPessoaConfigModel


def create_notificacao_pessoa_config(db: Session, notificacao_pessoa_config: NotificacaoPessoaConfigCreate):
    nova_notificacao_pessoa_config = NotificacaoPessoaConfigModel(**notificacao_pessoa_config.dict())
    db.add(nova_notificacao_pessoa_config)
    db.commit()
    db.refresh(nova_notificacao_pessoa_config)

    return nova_notificacao_pessoa_config


def find_all_notificacoes_pessoas_configs(db: Session) -> List[Any]:
    return db.query(notificacaoPessoaConfigModel).all()


def find_one_notificacao_pessoa_config(db: Session, notificacao_pessoa_config: int):
    return db.query(notificacaoPessoaConfigModel).filter(notificacaoPessoaConfigModel.id == notificacao_pessoa_config).first()
