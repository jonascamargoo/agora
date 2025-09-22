from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import models
from ..database import get_db

# Cria um "roteador". Podemos pensar nele como um "mini-FastAPI".
router = APIRouter(
    prefix="/channels",  # Adiciona um prefixo a todas as rotas deste roteador
    tags=["channels"]    # Adiciona uma tag para agrupar na documentação
)

@router.post("/", response_model=models.Channel)
def create_channel(channel: models.ChannelCreate, db: Session = Depends(get_db)):
    # Usando o novo método recomendado
    db_channel = models.Channel.model_validate(channel)
    
    db.add(db_channel)
    db.commit()
    db.refresh(db_channel)
    
    return db_channel

@router.get("/", response_model=List[models.Channel])
def read_channels(db: Session = Depends(get_db)):
    channels = db.query(models.Channel).all()
    return channels


