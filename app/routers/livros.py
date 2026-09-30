from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.livro import LivroCreate, LivroSchema
from app.database.conection import get_db  # Garanta que a importação do seu get_db está correta aqui
from app.services import livro_service     # Ajuste o import conforme a sua estrutura de pastas

router = APIRouter(
    prefix="/livros",
    tags=["livros"],
)


@router.get("/")
async def listar_livros(
    db: Session = Depends(get_db)
):
    return livro_service.listar_livros(db)


# Adicionar Livros
@router.post("/")
async def adicionar_livro(
    livro: LivroCreate,
    db: Session = Depends(get_db)
):
    return livro_service.adicionar_livro(livro, db)


# atualizar-livro
@router.put("/{index}")
async def atualizar_livro(
    index: int,
    livro: LivroCreate,
    db: Session = Depends(get_db)
):
    livro_db = livro_service.atualizar_livro(index, livro, db)
    
    if not livro_db:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
        
    return livro_db


# delete-livro
@router.delete("/{index}")
async def deletar_livro(
    index: int,
    db: Session = Depends(get_db)
):
    removido = livro_service.remover_livro(index, db)
    
    if not removido:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
        
    return {
        "message": "Livro removido com sucesso!!"
    }
