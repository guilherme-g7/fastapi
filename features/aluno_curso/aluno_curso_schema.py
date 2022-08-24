from pydantic import BaseModel


class AlunoCursoBase(BaseModel):
    ano_ingresso: str
    periodo_ingresso: str
    id_origem: int


class AlunoCursoCreate(AlunoCursoBase):
    pass


class AlunoCurso(AlunoCursoBase):
    id: int
    id_curso: int
    id_pessoa: int

    class Config:
        orm_mode = True
