from pydantic import BaseModel, Field

class LivroSchema(BaseModel):
    id: int
    titulo: str = Field(min_length=3, max_length=100)
    autor: str = Field(min_length=3, max_length=100)
    ano_publicacao: int

class LivroCreate(LivroSchema):
    pass

class LivroResponse(LivroSchema):
    id: int

    class Config:
        from_attributes = True