from fastapi import FastAPI, Path
from typing import Optional
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

inventory = {
    1: {
        "name": "Milk",
        "price": 34.89,
        "brand": "Highland"
    }
}

@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(None, description="This ID of the item you like to view")):
    return inventory[item_id]

@app.get('/get-by-name')
def get_item(name: str = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)