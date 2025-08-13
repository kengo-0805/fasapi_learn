from fastapi import FastAPI
from pydantic import BaseModel, Field

class Data(BaseModel):
    x: float
    y: float

app = FastAPI()  # FastAPIインスタンス化 

@app.get("/")
def index():
    return {"message": "Hello, Deta!"}

@app.post("/")
def calc(data: Data):
    z = data.x * data.y
    return {"result": z}