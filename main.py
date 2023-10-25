from fastapi import FastAPI
from router import curso_router

app = FastAPI(
    title = "Tarefa de POO/Prova com atualizações. Discente: Santiago da Rocha Souza",
    description  = "Criação de CRUD usando o modelo CURSO - Foi feito a correção onde ao atualizar, listar por id e deletar, os mesmo puxavam por índice e não pelo próprio id. Sendo assim ao inserir o código_id = 1 não retornava nada pois era a posição 0, colocando no curso_id = 0, retornava o curso_id = 1, não seria algo que deixaria de funcionar, mas deixaria o código com erro de lógica.",
    version = "0.1.1"

)

app.include_router(curso_router.router, prefix = "/Cursos")