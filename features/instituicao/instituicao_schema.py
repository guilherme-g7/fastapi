from json import JSONEncoder

from pydantic import BaseModel
from features.campus.campus_schema import Campus, CampusCreate


class InstituicaoBase(BaseModel):
    cnpj: str
    razao_social: str
    fantasia: str
    email: str
    cod_mec: str
    telefone: str


class InstituicaoCreate(InstituicaoBase):
    pass


class Instituicao(InstituicaoBase):
    id: int
    campus: list[Campus] = []

    class Config:
        orm_mode = True

