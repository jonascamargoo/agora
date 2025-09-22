from fastapi import FastAPI
from .database import init_db

# Função que será executada na inicialização
def on_startup():
    print("Creating tables in the database...")
    init_db()
    print("Tables created successfully.")
    

# Cria a aplicação FastAPI e associa o evento de startup
app = FastAPI(
    title="Projeto Agora",
    on_startup=[on_startup]
)

@app.get("/")
def get_root():
    return {"status": "servidor online"}
