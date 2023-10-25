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
@router.get("/{curso_id}", response_model=CursoModel)
def listar_curso_por_id(curso_id: int):
    curso_encontrado = None
    for curso in cursos:
        if curso.id == curso_id:
            curso_encontrado = curso
            break

    if curso_encontrado is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")

    return curso_encontrado

#Método onde cadastra o curso:
@router.post("/cursos/", response_model= CursoModel)
def cadastrar_cursos(curso: CursoModel):
    cursos.append(curso)
    return curso

#Método onde atualiza um curso:
@router.put("/cursos/{curso_id}", response_model=CursoModel)
def atualizar_cursos(curso_id: int, updated_curso: CursoModel):
    curso_encontrado = None
    for i, curso in enumerate(cursos):  # "i" , vai servir para saber em qual indice (posição) o curso esta percorrendo, e o Curso vai verificar se o número atribuido ao atributo id é igual ao curso_id.
        if curso.id == curso_id:  # Certifique-se de usar o atributo correto, como 'id' neste exemplo.
            curso_encontrado = curso
            cursos[i] = updated_curso
            break

    if curso_encontrado is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")

    return updated_curso


#Método onde deleta um curso:
@router.delete("/cursos/{curso_id}", response_model=CursoModel)
def deletar_cursos(curso_id: int):
    curso_encontrado = None
    for i, curso in enumerate(cursos):
        if curso.id == curso_id:
            curso_encontrado = curso
            break

    if curso_encontrado is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")

    cursos.pop(i)  # Remove o curso encontrado na posição i, identificando o id através da variável curso
    return curso_encontrado
