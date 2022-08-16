from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

cursos = [
    Curso(id=1,titulo='Algoritmo  e lógica de programação',aulas=122, horas=48),
    Curso(id=2,titulo='Progamação para leigos',aulas=212, horas=68),
    Curso(id=3,titulo='Teoria da Computação',aulas=322, horas=148),
    Curso(id=4,titulo='Lógica de programação',aulas=72, horas=36)
]