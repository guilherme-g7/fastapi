from pydantic import BaseModel

from features.curso.curso_schema import Curso


class PessoaBase(BaseModel):
    nome: str
    dt_nascimento: str
    cpf: str
    id_origem: int


class PessoaCreate(PessoaBase):
    cursos: list[Curso]


class Pessoa(PessoaBase):
    id: int
    cursos: list[Curso] = []

    class Config:
        orm_mode = True
