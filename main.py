from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel

class ShopInfo(BaseModel):
    name: str
    location: str

# データの構造を定義
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


class Data(BaseModel):
    ShopInfo: Optional[ShopInfo]
    items: List[Item]


app = FastAPI() # FastAPIインスタンス化 （APIの空箱を作っているようなイメージ）

@app.post("/")
async def index(data: Data): # 上で定義した形で入ってきて欲しい
    return {"data": data}