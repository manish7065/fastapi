from fastapi import FastAPI

from routers import blog,user



app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)

if __name__ =="__main__":
    # uvicorn.run(app, host='127.0.0.1',port=9000)
    uvicorn.run(app, host='0.0.0.0',port=9000)

# models.Base.metadata.create_all(engine) #will create table if dosent exist in db




# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blog'])
# def create(request: schemas.Blog,db: Session = Depends(get_db)):
#    new_blog= models.Blog(title=request.title,body=request.body,user_id=1)
#    db.add(new_blog)
#    db.commit()
#    db.refresh(new_blog)
#    return new_blog

# Deleting the record in db
# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blog'])
# def destroy(id,db:Session=Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with if {id} not found")
    
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'deleted'


# Updating the blog
# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['blog'])
# def update(id, request:schemas.Blog, db: Session = Depends(get_db)):
    
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with if {id} not found")
    
#     blog.update({'title':request.title,'body':request.body})
    
#     db.commit()
#     return 'updated sucessfully'




# @app.get('/blog',response_model=List[schemas.ShowBlog],tags=['blog'])
# def all(db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs
    

# @app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=['blog'])
# def show(id, db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     # if not blog:
#     #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#     #     detail=f"Blog with the id {id} is not available"
#     #     )

#     return blog



# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# @app.post('/user',response_model=schemas.ShowUser,tags=['user'])
# def create_user(request: schemas.User, db : Session=Depends(get_db)):
#     # hashedPassword = pwd_context.hash(request.password)
#     new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
#     # print(f"printing the new_user: {new_user}")
#     db.add(new_user)
#     # {'name':name,'email':email,'passwor':password}
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}',response_model=schemas.ShowUser,tags=['user'])
# def show_user(id, db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"User with the  id  {id} dosen't exist")
#     return user

