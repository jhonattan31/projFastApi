from fastapi import APIRouter
import string
from tokenize import String
from typing import Optional, List, Any, Dict, Tuple
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Response
from fastapi import status
from fastapi import Path
from fastapi import Query
from models import models

router = APIRouter()

@router.get('/cursos', response_model = List[models.Curso], description='Retorna todos os cursos ou uma lista vazia', summary='Retorna todos os cursos ou uma lista vazia')
async def get_cursos():
    return models.cursos

@router.get('/cursos/{curso_id}', response_model = models.Curso, description='Retorna um curso especifico passado por parametro', summary='Retorna um curso especifico passado por parametro')
async def get_cursos(curso_id: int = Path(default=None, title='ID do Curso', description='Deve ser entre 1 e 2', gt=0, lt=3)):
    try:    
        curso = models.cursos.__getitem__(curso_id)
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

@router.post('/cursos', response_model = models.Curso, status_code=status.HTTP_201_CREATED, description='Cadastrar um curso novo ao banco', summary='Cadastrar um curso novo ao banco') 
async def post_cursos(curso: models.Curso):
    next_id: int = len(models.cursos) + 1
    curso.id = next_id
    models.cursos.append(curso)
    return curso

@router.put('/cursos/{curso_id}', response_model = models.Curso, description='Atualiza um curso especifico passado por parametro', summary='Atualiza um curso especifico passado por parametro')
async def update_curso(curso_id: int, curso: models.Curso):
    if(curso_id in models.cursos):
        curso.id = curso_id
        models.cursos.append(curso)
        return models.cursos
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

@router.get('/calculadora')
async def calculadora(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), c: Optional[int] = None):
    resultado = a + b + c
    return {'Resultado': resultado }


@router.delete('/cursos/{curso_id}', description='Deleta um curso especifico passado por parametro', summary='Deleta um curso especifico passado por parametro')
async def delete_cursos(curso_id: int):
    if(curso_id in models.cursos):
        models.cursos.pop(curso_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


