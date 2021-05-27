from fastapi import FastAPI

# create instance
app = FastAPI()

# decoration
@app.get('/')
def index():
    return {'data': {'name': 'Malindu'}}

@app.get('/about')
def about():
    return {'data': 'about page'}