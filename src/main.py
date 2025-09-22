# app/main.py

from fastapi import FastAPI
from .database import init_db

# Função que será executada na inicialização
def on_startup():
    print("Criando tabelas no banco de dados...")
    init_db()
    print("Tabelas criadas com sucesso.")

# Cria a aplicação FastAPI e associa o evento de startup
app = FastAPI(
    title="Projeto Agora",
    on_startup=[on_startup]
)

@app.get("/")
def get_root():
    return {"status": "servidor online"}

# ... (seus outros endpoints virão aqui)