from sqlalchemy.orm import Session

from app.database.models import LivroModel
from app.schemas.livro import LivroCreate


def listar_livros(db: Session):
    return db.query(LivroModel).all()


def buscar_livro(id: int, db: Session):
    return db.query(LivroModel).filter(LivroModel.id == id).first()

def adicionar_livro(livro: LivroCreate, db: Session):
    novo_livro = LivroModel(
        titulo = livro.titulo,
        autor = livro.autor
    )

db.add(novo_livro)
db.commit()
db.refresh(novo_livro)

return novo_livro


def atualizar_livro(id: int, livro:LivroCreate, db:Session):
    livro_db = buscar_livro(id, db)

    if not livro_db:
        return None

    livro_db.titulo = livro.titulo
    livro_db.autor = livro.autor

    db.commit()
    db.refresh(livro_db)

    return livro_db

def remover_livro(id:int, db:session):
    livro_db = buscar_livro(id, db)

    if not livro_db:
        return False

    db.delete(livro_db)
    db.commit()

    return True