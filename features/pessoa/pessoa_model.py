from pydantic import BaseModel

from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

import features.curso.curso_model as curso


class PessoaModel(Base):
    __tablename__ = "pessoas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(500))
    dt_nascimento = Column(Date)
    cpf = Column(String(255))
    id_origem = Column(Integer)

    cursos = relationship('CursoModel', back_populates="pessoa")
    alunos_cursos = relationship('AlunoCursoModel', back_populates="pessoa")
