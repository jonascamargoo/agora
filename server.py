from fastapi import FastAPI

app = FastAPI(title="Sistemas Distribuídos Chat")

@app.get("/")
def get_root():
    return {"status": "servidor online"}

# uvicorn server:app --reload