from pydantic import BaseModel


class DisciplinaHorarioBase(BaseModel):
    modalidade: str
    data: str
    hora_inicial: str
    hora_final: str
    sala: str
    id_origem: int


class DisciplinaHorarioCreate(DisciplinaHorarioBase):
    pass


class DisciplinaHorario(DisciplinaHorarioBase):
    id: int
    id_disciplina: int

    class Config:
        orm_mode = True
