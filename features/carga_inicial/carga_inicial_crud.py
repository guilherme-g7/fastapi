from typing import Dict, Union
from sqlalchemy.orm import Session

def create_carga_inicial(json: Dict[str, Union[float, int, str]], db: Session):
    print(json)