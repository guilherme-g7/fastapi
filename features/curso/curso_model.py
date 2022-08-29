from pydantic import BaseModel

from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from features.pessoa.pessoa_model import PessoaModel


class CursoModel(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True, index=True)
    id_campus = Column(Integer, ForeignKey("campus.id"))
    id_pessoa = Column(Integer, ForeignKey("pessoas.id"))
    matriz = Column(String(255))
    turno = Column(String(255))
    modalidade = Column(String(255))
    nivel_ensino = Column(String(255))
    id_origem = Column(Integer)

    campus = relationship("CampusModel", back_populates="cursos")
    pessoa = relationship('PessoaModel', back_populates="cursos")
    calendarios_academicos = relationship('CalendarioAcademicoModel', back_populates='curso')
    alunos_cursos = relationship('AlunoCursoModel', back_populates='curso')
    disciplinas = relationship('DisciplinaModel', back_populates='curso')
