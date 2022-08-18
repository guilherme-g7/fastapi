from pydantic import BaseModel
from typing import List

from db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..campus.campus_model import Campus, CampusCreate


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


class InstituicaoBase(BaseModel):
    cnpj: str
    razao_social: str
    fantasia: str
    email: str
    cod_mec: str
    telefone: str


class InstituicaoCreate(InstituicaoBase):
    campus: List[Campus]


class Instituicao(InstituicaoBase):
    id: int
    campus: List[Campus] = []

    class Config:
        orm_mode = True

