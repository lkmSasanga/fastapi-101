from fastapi import FastAPI
from typing import Optional

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
def show(id):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}


