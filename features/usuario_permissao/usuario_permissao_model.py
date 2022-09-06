from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class UsuarioPermissaoModel(Base):
    __tablename__ = 'usuarios_permissoes'
    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'), index=True)
    id_permissao = Column(Integer, ForeignKey('permissoes.id'), index=True)

    usuario = relationship("UsuarioModel", back_populates='usuarios_permissoes')
    permissao = relationship("PermissaoModel", back_populates='usuarios_permissoes')
