from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class AlunoCursoSemestreModel(Base):
    __tablename__ = 'alu_cur_semestres'
    id = Column(Integer, primary_key=True, index=True)
    id_aluno_curso = Column(Integer, ForeignKey('alunos_cursos.id'))
    ano = Column(String(255))
    periodo = Column(String(255))
    id_origem = Column(Integer)

    aluno_curso = relationship('AlunoCursoModel', back_populates='alu_cur_semestres')
    alu_cur_sem_disciplinas = relationship('AlunoCursoSemestreDisciplinaModel', back_populates='alu_cur_semestre')
