from pydantic import BaseModel

from features.usuario_permissao.usuario_permissao_schema import UsuarioPermissao


class UsuarioBase(BaseModel):
    logado: bool
    id_origem: int


class UsuarioCreate(UsuarioBase):
    pass


class Usuario(UsuarioBase):
    id: int
    id_instituicao: int
    id_pessoa: int
    permissoes: list[UsuarioPermissao]

    class Config:
        orm_mode = True
