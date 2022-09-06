from pydantic import BaseModel

from features.usuario_permissao.usuario_permissao_schema import UsuarioPermissao


class PermissaoBase(BaseModel):
    nome: bool
    id_origem: int


class PermissaoCreate(PermissaoBase):
    pass


class Permissao(PermissaoBase):
    id: int
    usuarios: list[UsuarioPermissao]

    class Config:
        orm_mode = True
