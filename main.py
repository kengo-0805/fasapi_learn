from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI() # FastAPIインスタンス化 （APIの空箱を作っているようなイメージ）

# データの構造を定義
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

@app.post("/item/")
async def create_item(item: Item): # 上で定義した形で入ってきて欲しい
    