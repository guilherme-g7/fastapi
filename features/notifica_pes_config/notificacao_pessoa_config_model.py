from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table, Boolean
from sqlalchemy.orm import relationship


class NotificacaoPessoaConfigModel(Base):
    __tablename__ = 'notificacoes_pesssoas_configs'
    id = Column(Integer, primary_key=True, index=True)
    id_pessoa = Column(Integer, ForeignKey('pessoas.id'))
    notas = Column(String(255))
    avisos = Column(String(255))
    financeiro = Column(String(255))
    mkt = Column(String(255))
    bolsas = Column(String(255))

    pessoa = relationship("PessoaModel", back_populates='notificacoes_pesssoas_configs')


