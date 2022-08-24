from pydantic import BaseModel


class AlunoCursoSemestreBase(BaseModel):
    ano: str
    periodo: str
    id_origem: int


class AlunoCursoSemestreCreate(AlunoCursoSemestreBase):
    pass


class AlunoCursoSemestre(AlunoCursoSemestreBase):
    id: int
    id_aluno_curso: int

    class Config:
        orm_mode = True
