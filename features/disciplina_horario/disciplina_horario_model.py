from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date, Time
from sqlalchemy.orm import relationship


class DisciplinaHorarioModel(Base):
    __tablename__ = 'dis_horarios'
    id = Column(Integer, primary_key=True, index=True)
    id_disciplina = Column(Integer, ForeignKey('disciplinas.id'))
    modalidade = Column(String(255))
    data = Column(Date)
    hora_inicial = Column(Time)
    hora_final = Column(Time)
    sala = Column(String(255))
    id_origem = Column(Integer)

    disciplina = relationship('DisciplinaModel', back_populates='dis_horarios')
