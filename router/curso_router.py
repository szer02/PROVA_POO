from fastapi import APIRouter, HTTPException
from typing import List
from schema.curso_schema import CursoModel

router = APIRouter()

cursos = []

#Método onde é informado todos os cursos da lista:
@router.get("/cursos/", response_model = List[CursoModel])
def listar_cursos():
    return cursos

#Método para listar curso por ID
'''@router.get("/{curso_id}", response_model = CursoModel)
def listar_cursos_id(curso_id: int):
    if curso_id >= len(cursos):
        raise HTTPException(status_code= 404, detail="Curso não encontrado")
    curso_encontrado = cursos[curso_id]
    return curso_encontrado '''

#Método onde cadastra o curso:
@router.post("/cursos/", response_model= CursoModel)
def cadastrar_cursos(curso: CursoModel):
    cursos.append(curso)
    return curso

#Método onde atualiza um curso:
@router.put("/cursos/{curso_id}", response_model= CursoModel)
def atualizar_cursos(curso_id: int, updated_curso:  CursoModel):
    if curso_id >= len(cursos):
        raise HTTPException(status_code= 404, detail="Curso não encontrado")
    cursos[curso_id] = updated_curso
    return updated_curso

@router.delete("/cursos/{curso_id}", response_model = CursoModel)
def deletar_cursos(curso_id: int):
    if curso_id >= len(cursos):
        raise HTTPException(status_code = 404, detail = "Curso não encontrad")
    deleted_curso = cursos.pop(curso_id)
    return deleted_curso