from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship


class UsuarioModel(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    id_instituicao = Column(Integer, ForeignKey("instituicoes.id"))
    id_pessoa = Column(Integer, ForeignKey('pessoas.id'))
    logado = Column(Boolean, default=False)
    id_origem = Column(Integer)

    instituicao = relationship("InstituicaoModel", back_populates="usuarios")
    pessoa = relationship('PessoaModel', back_populates='usuario')
    usuarios_permissoes = relationship("UsuarioPermissaoModel", back_populates='usuario')
