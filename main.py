from fastapi import FastAPI

# create instance
app = FastAPI()

# decoration
# base path
@app.get('/blog')
def index(limit):
    return {'data': f'{limit} blogs form db'}
    

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


