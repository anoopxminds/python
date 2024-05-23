from fastapi import FastAPI, Query, Body
from fastapi.encoders import jsonable_encoder
from uuid import UUID
from datetime import datetime, time, timedelta
import uvicorn
from enum import Enum
from pydantic import BaseModel
from typing import Optional
from typing import List, Union
from typing_extensions import Annotated

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
    tag: List[str] = []

@app.post("/items")
async def postItems(item: Item):
    item_dict = item.dict()
    if item.tax :
        price_with_tax = item.price * item.tax
        item_dict.update({"Price with Tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def updateItem(item_id: int, item:Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@app.get("/items")
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            alias= "item-query",
            title= "Query String",
            description= "Query string item for the search in database that have a good match",
            min_length= 3,
            max_length= 10
        )
    ] = None
):
    result = {"items": [{"item_id": "Foo"}, {"Item_id": "Bar"}]}
    if q:
        result.update({"q": q})
    return result
    
    
items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items_list/{item_id}", response_model=Item)
async def read_item_list(item_id: str):
    return items[item_id]
    
@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id:str, item:Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
    

@app.put("/item/{item_id}")
async def put_items(
    item_id : UUID,
    start_date_time: Annotated[datetime, Body()],
    end_date_time: Annotated[datetime, Body()],
    after_process: Annotated[timedelta, Body()],
    repeat_at: Annotated[Union[time, None], Body()] = None
    ):
    start_process = start_date_time + after_process
    duration =    end_date_time - start_process
    return {
        "item_id": item_id,
        "start_date_time": start_date_time,
        "end_date_time": end_date_time,
        "process_after": after_process,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration
    }



if __name__ == "__main__":
    uvicorn.run('main:app', host='localhost', port=8080, reload=True)