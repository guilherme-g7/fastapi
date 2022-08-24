from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

import features.campus.campus_model
import features.curso.curso_model


class CalendarioAcademicoModel(Base):
    __tablename__ = 'calendarios_academicos'
    id = Column(Integer, primary_key=True, index=True)
    id_campus = Column(Integer, ForeignKey('campus.id'))
    id_curso = Column(Integer, ForeignKey('cursos.id'))
    data_inicio = Column(DateTime)
    data_fim = Column(DateTime)
    atividade = Column(String(255))
    tipo = Column(String(255))

    campus = relationship('CampusModel', back_populates='calendarios_academicos')
    curso = relationship('CursoModel', back_populates='calendarios_academicos')
