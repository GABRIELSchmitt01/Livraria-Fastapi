from pydantic import BaseModel, ConfigDict, Field


class LivroCreate(BaseModel):
    titulo: str = Field(min_length=3, max_length=100)
    autor: str = Field(min_length=3, max_length=100)
    ano_publicacao: int


class LivroResponse(LivroCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


# Schema usado para entrada de dados: o banco gera o id automaticamente.
LivroSchema = LivroCreate
