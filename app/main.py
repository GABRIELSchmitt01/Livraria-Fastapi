from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.database.conection import engine
from app.database.models import Base
from app.routers import livros

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Biblioteca FastAPI")
app.include_router(livros.router)

frontend_dir = Path(__file__).parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(frontend_dir / "index.html")
