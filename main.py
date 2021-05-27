from fastapi import FastAPI

# create instance
app = FastAPI()

# decoration
# base path
@app.get('/')
def index():
    return {'data': {'name': 'Blog List'}}


# about path
@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def show(id):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}


