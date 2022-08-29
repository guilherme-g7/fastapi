from pydantic import BaseModel

from features.permissao.permissao_schema import Permissao


class UsuarioBase(BaseModel):
    logado: bool
    id_origem: int


class UsuarioCreate(UsuarioBase):
    pass


class Usuario(UsuarioBase):
    id: int
    id_instituicao: int
    id_pessoa: int
    permissoes: list[Permissao]

    class Config:
        orm_mode = True
