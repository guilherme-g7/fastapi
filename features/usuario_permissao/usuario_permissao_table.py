from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Table
from sqlalchemy.orm import relationship


usuarios_permissoes = Table('usuarios_permissoes', Base.metadata,
                            Column('id', primary_key=True),
                            Column('id_usuario', ForeignKey('usuarios.id')),
                            Column('id_permissao', ForeignKey('permissoes.id'))
                            )
