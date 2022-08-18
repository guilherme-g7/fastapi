from re import I
from fastapi import APIRouter
from features.instituicao import instituicao_controller
from features.campus import campus_controller
from features.carga_inicial import carga_inicial_controller

router = APIRouter()

router.include_router(instituicao_controller.router, prefix='/api/v1', tags=['Instituição'])
router.include_router(campus_controller.router, prefix='/api/v1', tags=['Campus'])
router.include_router(carga_inicial_controller.router, prefix='/api/v1', tags=['Carga Inicial'])