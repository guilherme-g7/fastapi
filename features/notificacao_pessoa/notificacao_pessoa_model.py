from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table, Boolean
from sqlalchemy.orm import relationship


class NotificacaoPessoaModel(Base):
    __tablename__ = 'notificacoes_pessoas'
    id = Column(Integer, primary_key=True, index=True)
    id_pessoa = Column(Integer, ForeignKey('pessoas.id'))
    id_notificacao = Column(Integer, ForeignKey('notificacoes.id'))
    titulo = Column(String(2000))
    conteudo = Column(String(5000))
    lido = Column(Boolean, default=False)
    urgencia = Column(String(255))

    pessoa = relationship("PessoaModel", back_populates='notificacoes_pessoas')
    notificacao = relationship("NotificacaoModel", back_populates='notificacoes_pessoas')


