from fastapi import FastAPI, HTTPException
from app.schemas.livro import LivroSchema
from app.database.conection import engine
from app.routers import livros
from app.database.models import Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(livros.router)


@app.get("/") 
async def home():
    return {"message": "Bem-vindo à API de livros!"}



