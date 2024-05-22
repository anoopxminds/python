from fastapi import FastAPI
import uvicorn
from enum import Enum
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/hello")
async def root():
    return {"Message": "Hello Wrold ! and Test python3 virtual environment"}

class FoodEnum(str, Enum):
    
    vegiterian = "vegiterian"
    nonvegiterian = "nonvegiterian"
    fastfood = "fastfood"

    
@app.get("/food/{food_item}")
async def getFood(food_name: FoodEnum):
    
    if food_name == FoodEnum.vegiterian:
        return {"Food Item": food_name, "Message": "Always healthy food",}
    
    if food_name.value == "nonvegiterian":
        return {"Food Item": food_name, "Message": "Always non-healthy food",}
    
    return {"Food Item": food_name, "Message": "Always non-healthy food",}
    
class Item(BaseModel):
    name:str
    description: Optional[str] = None
    price:float
    tax: Optional[float] = None

@app.post("/items")
async def postItems(item: Item):
    item_dict = item.dict()
    if item.tax :
        price_with_tax = item.price * item.tax
        item_dict.update({"Price with Tax": price_with_tax})
    return item_dict


if __name__ == "__main__":
    uvicorn.run('main:app', host='localhost', port=8080, reload=True)