from pydantic import BaseModel


class NotificacaoPessoaConfigBase(BaseModel):
    notas: str
    avisos: str
    financeiro: str
    mkt: str
    bolsas: str


class NotificacaoPessoaConfigCreate(NotificacaoPessoaConfigBase):
    pass


class NotificacaoPessoaConfig(NotificacaoPessoaConfigBase):
    id: int
    id_pessoa: int

    class Config:
        orm_mode = True
