from pydantic import BaseModel
from features.campus.campus_schema import Campus


class InstituicaoBase(BaseModel):
    cnpj: str
    razao_social: str
    fantasia: str
    email: str
    cod_mec: str
    telefone: str


class InstituicaoCreate(InstituicaoBase):
    campus: list[Campus]


class Instituicao(InstituicaoBase):
    id: int
    campus: list[Campus] = []

    class Config:
        orm_mode = True
