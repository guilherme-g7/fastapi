from typing import List, Any

from .pessoa_model import PessoaModel
from sqlalchemy.orm import Session

from .pessoa_schema import PessoaCreate

pessoaModel = PessoaModel


def create_pessoa(db: Session, pessoa: PessoaCreate):
    nova_pessoa = PessoaModel(**pessoa.dict())
    db.add(nova_pessoa)
    db.commit()
    db.refresh(nova_pessoa)

    return nova_pessoa


def find_all_pessoa(db: Session) -> List[Any]:
    return db.query(pessoaModel).all()


def find_one_pessoa(db: Session, pessoa_id: int):
    return db.query(pessoaModel).filter(pessoaModel.id == pessoa_id).first()
