from pydantic import BaseModel

from db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import inspect

from features.campus.campus_model import CampusModel


class InstituicaoModel(Base):
    __tablename__ = "instituicoes"
    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String(14))
    razao_social = Column(String(500))
    fantasia = Column(String(500))
    email = Column(String(255))
    cod_mec = Column(String(50))
    telefone = Column(String(20))

    campus = relationship("CampusModel", back_populates="instituicao")
    usuarios = relationship("UsuarioModel", back_populates="instituicao")

