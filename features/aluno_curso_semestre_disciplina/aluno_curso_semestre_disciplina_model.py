from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class AlunoCursoSemestreDisciplinaModel(Base):
    __tablename__ = 'alu_cur_sem_disciplinas'
    id = Column(Integer, primary_key=True, index=True)
    id_alu_cur_semestre = Column(Integer, ForeignKey('alu_cur_semestres.id'))
    id_disciplina = Column(Integer, ForeignKey('disciplinas.id'))
    media_parcial = Column(String(255))
    media_final = Column(String(255))
    situacao = Column(String(255))
    percentual_faltas = Column(String(255))
    id_origem = Column(Integer)

    alu_cur_semestre = relationship('AlunoCursoSemestreModel', back_populates='alu_cur_sem_disciplinas')
    disciplina = relationship('DisciplinaModel', back_populates='alu_cur_sem_disciplinas')
    alu_cur_sem_dis_notas = relationship('AlunoCursoSemestreDisciplinaNotaModel', back_populates='alu_cur_sem_disciplina')
