from fastapi import APIRouter, Depends
from app.database import get_db
from app import models, schemas, oauth2
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/me", response_model=schemas.UserResponse)
def get_me(db: Session = Depends(get_db), user_id: str = Depends(oauth2.require_user)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user