from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Time
from sqlalchemy.orm import relationship


class DisciplinaProfessorModel(Base):
    __tablename__ = 'disciplinas_professores'
    id = Column(Integer, primary_key=True, index=True)
    id_disciplina = Column(Integer, ForeignKey('disciplinas.id'))
    id_pessoa = Column(Integer, ForeignKey('pessoas.id'))
    tipo = Column(String(255))
    id_origem = Column(Integer)

    pessoa = relationship('PessoaModel', back_populates='dis_professores')
    disciplina = relationship('DisciplinaModel', back_populates='dis_professores')
