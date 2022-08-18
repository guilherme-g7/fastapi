from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class CampusModel(Base):
    __tablename__ = "campus"
    id = Column(Integer, primary_key=True, index=True)
    id_instituicao = Column(Integer, ForeignKey("instituicoes.id"))
    nome = Column(String(255))
    endereco = Column(String(500))
    email = Column(String(255))
    id_origem = Column(Integer)

    instituicao = relationship("InstituicaoModel", back_populates="campus")


class CampusBase(BaseModel):
    nome: str
    endereco: str
    email: str
    id_origem: int


class CampusCreate(CampusBase):
    pass


class Campus(CampusBase):
    id: int
    id_instituicao: int

    class Config:
        orm_mode = True

