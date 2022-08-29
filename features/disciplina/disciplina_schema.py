from pydantic import BaseModel


class DisciplinaBase(BaseModel):
    carga_horaria: str
    turma: str
    descricao: str
    id_origem: int


class DisciplinaCreate(DisciplinaBase):
    pass


class Disciplina(DisciplinaBase):
    id: int
    id_curso: int

    class Config:
        orm_mode = True
