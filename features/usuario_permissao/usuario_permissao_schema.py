from pydantic import BaseModel


class UsuarioPermissaoBase(BaseModel):
    id_usuario: int
    id_permissao: int


class UsuarioPermissaoCreate(UsuarioPermissaoBase):
    pass


class UsuarioPermissao(UsuarioPermissaoBase):
    id: int

    class Config:
        orm_mode = True
