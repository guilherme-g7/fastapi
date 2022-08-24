from pydantic import BaseModel


class AlunoCursoSemestreDisciplinaBase(BaseModel):
    media_parcial: str
    media_final: str
    situacao: str
    percentual_faltas: str
    id_origem: int


class AlunoCursoSemestreDisciplinaCreate(AlunoCursoSemestreDisciplinaBase):
    pass


class AlunoCursoSemestreDisciplina(AlunoCursoSemestreDisciplinaBase):
    id: int
    id_alu_cur_semestre: int
    id_disciplina: int

    class Config:
        orm_mode = True
