from pydantic import BaseModel


class DisciplinaProfessorBase(BaseModel):
    tipo: str
    id_origem: int


class DisciplinaProfessorCreate(DisciplinaProfessorBase):
    pass


class DisciplinaProfessor(DisciplinaProfessorBase):
    id: int
    id_disciplina: int
    id_pessoa: int

    class Config:
        orm_mode = True
