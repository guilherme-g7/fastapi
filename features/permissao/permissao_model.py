from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


class PermissaoModel(Base):
    __tablename__ = 'permissoes'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(500))
    id_origem = Column(Integer)

    usuarios = relationship("UsuarioModel", secondary="usuarios_permissoes", back_populates='permissoes')


