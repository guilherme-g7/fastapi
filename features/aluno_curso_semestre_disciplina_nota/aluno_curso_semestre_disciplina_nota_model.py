from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class AlunoCursoSemestreDisciplinaNotaModel(Base):
    __tablename__ = 'alu_cur_sem_dis_notas'
    id = Column(Integer, primary_key=True, index=True)
    id_alu_cur_sem_disciplina = Column(Integer, ForeignKey('alu_cur_sem_discip.id'))
    nome = Column(String(255))
    valor = Column(String(255))
    peso = Column(String(255))
    id_origem = Column(Integer)

    alu_cur_sem_disciplina = relationship('AlunoCursoSemestreDisciplinaModel', back_populates='alu_cur_sem_dis_notas')
