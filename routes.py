from re import I
from fastapi import APIRouter
from features.instituicao import instituicao_controller
from features.campus import campus_controller
from features.carga_inicial import carga_inicial_controller
from features.pessoa import pessoa_controller
from features.curso import curso_controller
from features.calendario_academico import calendario_academico_controller

router = APIRouter()

PREFIX = '/api/v1'

router.include_router(instituicao_controller.router, prefix=PREFIX, tags=['Instituição'])
router.include_router(campus_controller.router, prefix=PREFIX, tags=['Campus'])
router.include_router(curso_controller.router, prefix=PREFIX, tags=['Cursos'])
router.include_router(pessoa_controller.router, prefix=PREFIX, tags=['Pessoas'])
router.include_router(calendario_academico_controller.router, prefix=PREFIX, tags=['Calendário Acadêmico'])
router.include_router(carga_inicial_controller.router, prefix=PREFIX, tags=['Carga Inicial'])
