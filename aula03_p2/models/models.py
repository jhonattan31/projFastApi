from typing import Optional
from wsgiref.validate import validator
from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value: str):
        palavras = value.split(' ')
        if len(palavras) < 2:
            raise ValueError('O titulo deve conter mais do que 2 palavras')

        return value
    
    @validator('aulas')
    def validar_aulas(cls, value: int):
        if value < 12:
            raise ValueError('O curso deve possui mais de 12 aulas')

        return value

    @validator('horas')
    def validar_horas(cls, value: int):
        if value < 12:
            raise ValueError('O curso deve possui mais de 12 horas/aula')

        return value

cursos = [
    Curso(id=1,titulo='Algoritmo  e lógica de programação',aulas=122, horas=48),
    Curso(id=2,titulo='Progamação para leigos',aulas=212, horas=68),
    Curso(id=3,titulo='Teoria da Computação',aulas=322, horas=148),
    Curso(id=4,titulo='Lógica de programação',aulas=72, horas=36)
]