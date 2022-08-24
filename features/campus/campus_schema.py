from pydantic import BaseModel

from features.curso.curso_schema import Curso


class CampusBase(BaseModel):
    nome: str
    endereco: str
    email: str
    id_origem: int


class CampusCreate(CampusBase):
    cursos: list[Curso]


class Campus(CampusBase):
    id: int
    id_instituicao: int
    cursos: list[Curso] = []

    class Config:
        orm_mode = True
