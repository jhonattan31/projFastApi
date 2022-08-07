from fastapi import FastAPI

app = FastAPI()

cursos = {
    1: {
        "titulo": "Progamação para leigos",
        "aulas": 112,
        "horas": 64
    },
    2: {
        "titulo": "Algoritmo  e lógica de programação",
        "aulas": 178,
        "horas": 100
    },
}