from typing import List

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from features.curso.curso_model import CursoModel


class CampusModel(Base):
    __tablename__ = "campus"
    id = Column(Integer, primary_key=True, index=True)
    id_instituicao = Column(Integer, ForeignKey("instituicoes.id"))
    nome = Column(String(255))
    endereco = Column(String(500))
    email = Column(String(255))
    id_origem = Column(Integer)

    instituicao = relationship("InstituicaoModel", back_populates="campus")
    cursos = relationship('CursoModel', back_populates="campus")
    calendarios_academicos = relationship('CalendarioAcademicoModel', back_populates='campus')
    notificacoes = relationship('NotificacaoModel', back_populates='campus')



