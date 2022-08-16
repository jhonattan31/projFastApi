from router import curso_router
from router import usuario_router
from fastapi import FastAPI

app = FastAPI(title='Api de cursos da udemy', version='0.0.1', description='Uma api para estudo do fastapi')
app.include_router(curso_router.router, tags=['cursos'])
app.include_router(usuario_router.router, tags=['usuarios'])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=9023, debug=True, reload=True)