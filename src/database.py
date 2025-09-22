# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine

from .config import DATABASE_URL


# O "engine" é o ponto de entrada para o banco de dados.
# Ele gerencia as conexões.
engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)

# Cada instância de SessionLocal será uma sessão com o banco de dados.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Usaremos isso mais tarde para nossos modelos ORM (se necessário).
Base = declarative_base()

# Função para obter uma sessão do banco de dados (Dependency)
# Este é o padrão "sessão por requisição"
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

