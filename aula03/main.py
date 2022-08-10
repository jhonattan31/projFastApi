from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Response
from fastapi import status

from models import Curso

app = FastAPI()


cursos = {
    1: {
        "id": 1,
        "titulo": "Progamação para leigos",
        "aulas": 112,
        "horas": 64
    },
    2: {
        "id": 2,
        "titulo": "Algoritmo  e lógica de programação",
        "aulas": 178,
        "horas": 100
    },
}


@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_cursos(curso_id: int):
    try:    
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')

@app.post('/cursos', status_code=status.HTTP_201_CREATED) 
async def post_cursos(curso: Curso):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos[next_id] = curso
    return curso

@app.put('/cursos/{curso_id}')
async def update_curso(curso_id: int, curso: Curso):
    if(curso_id in cursos):
        curso.id = curso_id
        cursos[curso_id] = curso
        return cursos
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@app.delete('/cursos/{curso_id}')
async def delete_cursos(curso_id: int):
    if(curso_id in cursos):
        cursos.pop(curso_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=9023, debug=True, reload=True)
