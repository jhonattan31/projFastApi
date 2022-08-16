from fastapi import APIRouter
router = APIRouter()

@router.get('/usuarios', description='Retorna todos os usuarios ou uma lista vazia', summary='Retorna todos os usuarios ou uma lista vazia')
async def get_usuarios():
    return {'info': 'Lista de usuarios disponiveis'}