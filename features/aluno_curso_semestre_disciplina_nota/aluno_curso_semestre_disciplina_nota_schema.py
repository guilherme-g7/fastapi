from pydantic import BaseModel


class AlunoCursoSemestreDisciplinaNotaBase(BaseModel):
    nome: str
    valor: str
    peso: str
    id_origem: int


class AlunoCursoSemestreDisciplinaNotaCreate(AlunoCursoSemestreDisciplinaNotaBase):
    pass


class AlunoCursoSemestreDisciplinaNota(AlunoCursoSemestreDisciplinaNotaBase):
    id: int
    id_alu_cur_sem_disciplina: int

    class Config:
        orm_mode = True
