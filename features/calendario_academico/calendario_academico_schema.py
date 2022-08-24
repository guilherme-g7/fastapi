from pydantic import BaseModel


class CalendarioAcademicoBase(BaseModel):
    data_inicio: str
    data_fim: str
    atividade: str
    tipo: str


class CalendarioAcademicoCreate(CalendarioAcademicoBase):
    pass


class CalendarioAcademico(CalendarioAcademicoBase):
    id: int
    id_campus: int
    id_curso: int

    class Config:
        orm_mode = True
