from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from fastapi.param_functions import Query
from pydantic import BaseModel
from pydantic.types import StrIntFloat
import uvicorn

# create instance
app = FastAPI()

# decoration
# base path
@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str] = None):

    if published:
        return {'data': f'{limit} published blogs form db'}
    else:
        return {'data': f'{limit} blogs from the db'}
    

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


# about path
@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def show(id, limit=10):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created as {blog.title}'}

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {}

@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(None, description="This ID of the item you like to view", gt=0)):
    return inventory[item_id]

@app.get('/get-by-name')
def get_item(name: Optional[str] = Query(None, title="Name", description="Name of item.")): 
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item name not found!")




@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item ID already exists!")
    
    inventory[item_id] = item
    return inventory[item_id]



@app.put('/update-item/{item_id}')
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exists!")

    if item.name != None:
        inventory[item_id].name = item.name

    if item.price != None:
        inventory[item_id].price = item.price

    if item.brand != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]


@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the item to delete", gt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exists!")


    del inventory[item_id]
    return {"Success": "Item deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)