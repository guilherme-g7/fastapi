from typing import Any

from pydantic import BaseModel


class InicialCampus(BaseModel):
    nome: str
    endereco: str
    email: str
    id_origem: int
    cursos: list[Any] = []
    calendarios_academicos: list[Any] = []
    notificacoes: list[Any] = []


class InicialInstituicao(BaseModel):
    cnpj: str
    razao_social: str
    fantasia: str
    email: str
    cod_mec: str
    telefone: str
    campus: list[InicialCampus]


class CargaInicial(BaseModel):
    instituicoes: list[InicialInstituicao]


