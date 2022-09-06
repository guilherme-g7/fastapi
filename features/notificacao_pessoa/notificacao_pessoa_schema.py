from pydantic import BaseModel


class NotificacaoPessoaBase(BaseModel):
    titulo: str
    conteudo: str
    lido: bool
    urgencia: str


class NotificacaoPessoaCreate(NotificacaoPessoaBase):
    pass


class NotificacaoPessoa(NotificacaoPessoaBase):
    id: int
    id_pessoa: int
    id_notificacao: int

    class Config:
        orm_mode = True
