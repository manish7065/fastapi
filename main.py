from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'index':'index page',
        'data':{'name':'manish'}}

@app.get('/blogs')
def blogs(limit=10,published:bool = True, sort: Optional[str]=None):
    if published:
        return {"data":f"return {limit} published blogs from DB"}
    else:
        return {"data":f"return {limit} blogs from DB"}

@app.get('/about')
def about():
    return {'data':{'about page'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':"unpublished" }

# Dynamic routing
@app.get('/blog/{id}')
def show(id:int):
    # Fetch blog with id = id
    return {'data': id}

@app.get('/blogs/{id}/comments')
def comments(id:int,limit = 10):
    return {'data':{'1',id,limit}}


# @app.get('/blog/unpublished')
# def unpublished():
#     return {'data':"unpublished" }

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return { 'data': f"Blog is created with title as {blog.title} and body:{blog.body}"}


if __name__ =="__main__":
    # uvicorn.run(app, host='127.0.0.1',port=9000)
    uvicorn.run(app, host='0.0.0.0',port=9000)
