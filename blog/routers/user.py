from fastapi import FastAPI,Depends,status,HTTPException,APIRouter
from .. import routers,schemas,models
from ..database import get_db
from sqlalchemy.orm import Session    
from ..hashing import Hash


router = APIRouter(
    tags=["Users"],
    prefix='/user'
    )




@router.post('/',response_model=schemas.ShowUser)
def create_user(request: schemas.User, db : Session=Depends(get_db)):
    # hashedPassword = pwd_context.hash(request.password)
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    # print(f"printing the new_user: {new_user}")
    db.add(new_user)
    # {'name':name,'email':email,'passwor':password}
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('//{id}',response_model=schemas.ShowUser)
def show_user(id, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with the  id  {id} dosen't exist")
    return user