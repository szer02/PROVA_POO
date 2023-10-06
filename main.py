from fastapi import FastAPI
from router import curso_router

app = FastAPI(
    title = "Prova de POO. Discente: Santiago da Rocha Souza",
    description  = "Criação de CRUD usando o modelo CURSO"
)

app.include_router(curso_router.router, prefix = "/Cursos")
