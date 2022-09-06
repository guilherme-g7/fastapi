from sqlalchemy.orm import Session

from features.campus.campus_model import CampusModel
from features.campus.campus_schema import CampusCreate, Campus
from features.carga_inicial.carga_inicial_schema import CargaInicial, InicialInstituicao, InicialCampus
from features.instituicao.instituicao_model import InstituicaoModel
from features.instituicao.instituicao_schema import InstituicaoCreate


def create_carga_inicial(db: Session, data: str):
    try:

        instituicoes = data['instituicoes']

        for i in instituicoes:
            instituicao_create = InstituicaoCreate(**i)
            instituicao = InstituicaoModel(**instituicao_create.dict())
            db.add(instituicao)
            db.flush()
            campusus = i['campus']
            for c in campusus:
                c['id_instituicao'] = instituicao.id
                campus_create = CampusCreate(**c)
                print(campus_create)
                campus = CampusModel(**campus_create.dict())
                db.add(campus)
                db.flush()

        db.commit()
        return True
    except:
        db.rollback()
        return False
