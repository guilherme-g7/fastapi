from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class NotificacaoModel(Base):
    __tablename__ = 'notificacoes'
    id = Column(Integer, primary_key=True, index=True)
    id_campus = Column(Integer, ForeignKey('campus.id'))
    id_curso = Column(Integer, ForeignKey('cursos.id'))
    id_disciplina = Column(Integer, ForeignKey('disciplinas.id'))
    status = Column(String(255))

    campus = relationship('CampusModel', back_populates='notificacoes')
    curso = relationship('CursoModel', back_populates='notificacoes')
    disciplina = relationship('DisciplinaModel', back_populates='notificacoes')
