from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.src.schemas.user_schema import LoginData, UserCreate
from app.src.services.auth_service import AuthService
from app.src.db.database import get_db


router = APIRouter()

@router.post("/login", response_model=dict, status_code=200)
def login(login_data: LoginData, db: Session = Depends(get_db)) -> dict:
    """
    Authenticate a user and return a JWT if valid.
    
    Args:
        login_data (LoginData): The data used for authenticating the user.
        db (Session): Dependency injection of the database session.

    Returns:
        dict: A dictionary containing the JWT token and token type.

    Raises:
        HTTPException: 401 error if authentication fails.
        HTTPException: 500 error if there is a problem in the authentication process.
    """
    auth_service = AuthService(db)
    try:
        token = auth_service.authenticate(login_data.email, login_data.password)
        if not token:
            raise HTTPException(status_code=401, detail="Incorrect email or password")
        return {"access_token": token, "token_type": "bearer"}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Authentication process failed: {e}")
    
    
@router.post("/register", response_model=dict, status_code=201)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)) -> dict:
    """
    Register a new user with the provided user data.
    
    Args:
        user_data (UserCreate): The data used to create a new user.
        db (Session): Dependency injection of the database session.
    
    Returns:
        dict: A dictionary representing the created user.
    """
    user_service = AuthService(db)
    try:
        new_user = user_service.create_user(user_data)
        return {"id": new_user.id, "email": new_user.email}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))