from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.database import init_db
from src.routers import channels

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Inicializando o banco de dados...")
    init_db()
    print("Banco de dados inicializado com sucesso.")
    yield
    print("Aplicação finalizada.")

app = FastAPI(
    title="Projeto Agora",
    lifespan=lifespan
)

# Inclui as rotas definidas em channels.py na nossa aplicação principal
app.include_router(channels.router)

@app.get("/")
def get_root():
    return {"status": "servidor online"}