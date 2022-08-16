import string
from tokenize import String
from typing import Optional, List, Any, Dict, Tuple
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Response
from fastapi import status
from fastapi import Path
from fastapi import Query
from models import Curso
from models import cursos

app = FastAPI(title='Api de cursos da udemy', version='0.0.1', description='Uma api para estudo do fastapi')


@app.get('/cursos', response_model = List[Curso], description='Retorna todos os cursos ou uma lista vazia', summary='Retorna todos os cursos ou uma lista vazia')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}', response_model = Curso, description='Retorna um curso especifico passado por parametro', summary='Retorna um curso especifico passado por parametro')
async def get_cursos(curso_id: int = Path(default=None, title='ID do Curso', description='Deve ser entre 1 e 2', gt=0, lt=3)):
    try:    
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

@app.post('/cursos', response_model = Curso, status_code=status.HTTP_201_CREATED, description='Cadastrar um curso novo ao banco', summary='Cadastrar um curso novo ao banco') 
async def post_cursos(curso: Curso):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos[next_id] = curso
    return curso

@app.put('/cursos/{curso_id}', response_model = Curso, description='Atualiza um curso especifico passado por parametro', summary='Atualiza um curso especifico passado por parametro')
async def update_curso(curso_id: int, curso: Curso):
    if(curso_id in cursos):
        curso.id = curso_id
        cursos[curso_id] = curso
        return cursos
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

@app.get('/calculadora')
async def calculadora(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), c: Optional[int] = None):
    resultado = a + b + c
    return {'Resultado': resultado }


@app.delete('/cursos/{curso_id}', description='Deleta um curso especifico passado por parametro', summary='Deleta um curso especifico passado por parametro')
async def delete_cursos(curso_id: int):
    if(curso_id in cursos):
        cursos.pop(curso_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=9023, debug=True, reload=True)
