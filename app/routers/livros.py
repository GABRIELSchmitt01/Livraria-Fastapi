from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.conection import get_db
from app.schemas.livro import LivroCreate, LivroResponse
from app.services import livro_services

router = APIRouter(prefix="/livros", tags=["livros"])


@router.get("/", response_model=list[LivroResponse])
def listar_livros(db: Session = Depends(get_db)):
    return livro_services.listar_livros(db)


@router.post("/", response_model=LivroResponse, status_code=status.HTTP_201_CREATED)
def adicionar_livro(livro: LivroCreate, db: Session = Depends(get_db)):
    return livro_services.adicionar_livro(livro, db)


@router.put("/{id}", response_model=LivroResponse)
def atualizar_livro(id: int, livro: LivroCreate, db: Session = Depends(get_db)):
    livro_db = livro_services.atualizar_livro(id, livro, db)
    if not livro_db:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro_db


@router.delete("/{id}")
def deletar_livro(id: int, db: Session = Depends(get_db)):
    removido = livro_services.remover_livro(id, db)
    if not removido:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return {"message": "Livro removido com sucesso"}
