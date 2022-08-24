from pydantic import BaseModel


class CursoBase(BaseModel):
    matriz: str
    turno: str
    modalidade: str
    nivel_ensino: str
    id_origem: int


class CursoCreate(CursoBase):
    pass


class Curso(CursoBase):
    id: int
    id_campus: int
    id_pessoa: int

    class Config:
        orm_mode = True
