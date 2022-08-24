from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class AlunoCursoModel(Base):
    __tablename__ = 'alunos_cursos'
    id = Column(Integer, primary_key=True, index=True)
    id_curso = Column(Integer, ForeignKey('cursos.id'))
    id_pessoa = Column(Integer, ForeignKey('pessoas.id'))
    ano_ingresso = Column(String(255))
    periodo_ingresso = Column(String(255))
    id_origem = Column(String(255))

    curso = relationship('CursoModel', back_populates='alunos_cursos')
    pessoa = relationship('PessoaModel', back_populates='alunos_cursos')
    alu_cur_semestres = relationship('AlunoCursoSemestreModel', back_populates='aluno_curso')
