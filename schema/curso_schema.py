from pydantic import BaseModel

class CursoModel(BaseModel):
    id : int
    titulo: str
    aulas: str
    horas: int
    dia: str
