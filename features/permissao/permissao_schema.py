from pydantic import BaseModel

from features.usuario.usuario_schema import Usuario


class PermissaoBase(BaseModel):
    nome: bool
    id_origem: int


class PermissaoCreate(PermissaoBase):
    pass


class Permissao(PermissaoBase):
    id: int
    usuarios: list[Usuario]

    class Config:
        orm_mode = True
