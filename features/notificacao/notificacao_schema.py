from pydantic import BaseModel


class NotificacaoBase(BaseModel):
    status: bool


class NotificacaoCreate(NotificacaoBase):
    pass


class Notificacao(NotificacaoBase):
    id: int
    id_campus: int
    id_curso: int
    id_disciplina: int

    class Config:
        orm_mode = True
