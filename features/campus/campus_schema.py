from pydantic import BaseModel

from features.calendario_academico.calendario_academico_schema import CalendarioAcademico
from features.curso.curso_schema import Curso
from features.notificacao.notificacao_schema import Notificacao


class CampusBase(BaseModel):
    nome: str
    endereco: str
    email: str
    id_origem: int


class CampusCreate(CampusBase):
    id_instituicao: int
    cursos: list[Curso]
    calendarios_academicos: list[CalendarioAcademico]
    notificacoes: list[Notificacao]


class Campus(CampusBase):
    id: int
    id_instituicao: int
    cursos: list[Curso] = []
    calendarios_academicos: list[CalendarioAcademico] = []
    notificacoes: list[Notificacao] = []

    class Config:
        orm_mode = True
