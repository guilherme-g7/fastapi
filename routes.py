from fastapi import APIRouter
from features.instituicao import instituicao_controller
from features.campus import campus_controller
from features.carga_inicial import carga_inicial_controller
from features.pessoa import pessoa_controller
from features.curso import curso_controller
from features.calendario_academico import calendario_academico_controller
from features.aluno_curso import aluno_curso_controller
from features.aluno_curso_semestre import aluno_curso_semestre_controller
from features.aluno_curso_semestre_disciplina import aluno_curso_semestre_disciplina_controller
from features.aluno_curso_semestre_disciplina_nota import aluno_curso_semestre_disciplina_nota_controller
from features.disciplina import disciplina_controller
from features.disciplina_horario import disciplina_horario_controller
from features.disciplina_professor import disciplina_professor_controller
from features.usuario import usuario_controller
from features.permissao import permissao_controller
from features.notificacao import notificacao_controller
from features.usuario_permissao import usuario_permissao_controller
from features.notificacao_pessoa import notificacao_pessoa_controller
from features.notifica_pes_config import notificacao_pessoa_config_controller

router = APIRouter()

PREFIX = '/api/v1'

router.include_router(instituicao_controller.router, prefix=PREFIX, tags=['Instituição'])
router.include_router(campus_controller.router, prefix=PREFIX, tags=['Campus'])
router.include_router(curso_controller.router, prefix=PREFIX, tags=['Cursos'])
router.include_router(pessoa_controller.router, prefix=PREFIX, tags=['Pessoas'])
router.include_router(calendario_academico_controller.router, prefix=PREFIX, tags=['Calendário Acadêmico'])
router.include_router(aluno_curso_controller.router, prefix=PREFIX, tags=['Aluno Curso'])
router.include_router(aluno_curso_semestre_controller.router, prefix=PREFIX, tags=['Aluno Curso Semestre'])
router.include_router(aluno_curso_semestre_disciplina_controller.router, prefix=PREFIX, tags=['Aluno Curso Semestre Disciplina'])
router.include_router(aluno_curso_semestre_disciplina_nota_controller.router, prefix=PREFIX, tags=['Aluno Curso Semestre Disciplina Notas'])
router.include_router(disciplina_controller.router, prefix=PREFIX, tags=['Disciplina'])
router.include_router(disciplina_horario_controller.router, prefix=PREFIX, tags=['Disciplina Horários'])
router.include_router(disciplina_professor_controller.router, prefix=PREFIX, tags=['Disciplina Professores'])
router.include_router(usuario_controller.router, prefix=PREFIX, tags=['Usuários'])
router.include_router(permissao_controller.router, prefix=PREFIX, tags=['Permissões'])
router.include_router(notificacao_controller.router, prefix=PREFIX, tags=['Notificações'])
router.include_router(notificacao_pessoa_controller.router, prefix=PREFIX, tags=['Notificações Pessoas'])
router.include_router(notificacao_pessoa_config_controller.router, prefix=PREFIX, tags=['Notificações Pessoas Configs'])
router.include_router(usuario_permissao_controller.router, prefix=PREFIX, tags=['Usuários Permissões'])
router.include_router(carga_inicial_controller.router, prefix=PREFIX, tags=['Carga Inicial'])
