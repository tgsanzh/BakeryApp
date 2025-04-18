from fastapi import APIRouter
from sqlalchemy.orm import Session

from Backend.backend.db_depends import get_db
from Backend.models.Users import Users
from Backend.schemas import *
from Backend.utils import *

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=TokenResponse)
def register_user(request: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(Users).filter(Users.phone == request.phone).first()
    if existing:
        raise HTTPException(status_code=400, detail="Phone already registered")

    user = Users(phone=request.phone, password=hash_password(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token(data={"sub": str(user.user_id)})
    return {"access_token": token, "token_type": "Bearer"}

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.phone == request.phone).first()
    if not user or not verify_password(request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid phone or password")

    token = create_access_token(data={"sub": str(user.user_id)})
    return {"access_token": token, "token_type": "Bearer"}

@router.get("/protected")
def protected_route(user_id: int = Depends(get_current_user)):
    return {"user_id": user_id}