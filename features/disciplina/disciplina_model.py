from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class DisciplinaModel(Base):
    __tablename__ = 'disciplinas'
    id = Column(Integer, primary_key=True, index=True)
    id_curso = Column(Integer, ForeignKey('cursos.id'))
    carga_horaria = Column(String(255))
    turma = Column(String(255))
    descricao = Column(String(500))
    id_origem = Column(Integer)

    curso = relationship('CursoModel', back_populates='disciplinas')
    dis_horarios = relationship('DisciplinaHorarioModel', back_populates='disciplina')
    dis_professores = relationship('DisciplinaProfessorModel', back_populates='disciplina')
    alu_cur_sem_disciplinas = relationship('AlunoCursoSemestreDisciplinaModel', back_populates='disciplina')
    notificacoes = relationship('NotificacaoModel', back_populates='disciplina')
