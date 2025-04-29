from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.crud import create_user, get_all_users, get_user_by_email, verify_user
from app.auth import create_access_token, verify_password, get_user_from_token
from app.schemas import UserCreate, UserInDB
from app.email import send_email
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/signup/")
async def signup(user_create: UserCreate):
    user_data = create_user(user_create)
    verification_link = f"http://localhost:8000/verify/{user_data['email']}"
    send_email(user_create.email, "Email Verification", f"Please verify your email: {verification_link}")
    return {"msg": "User created, please check your email for verification"}

@app.get("/verify/{email}")
async def verify_email(email: str):
    if verify_user(email):
        return {"msg": "Email verified successfully"}
    else:
        raise HTTPException(status_code=400, detail="Verification failed")

@app.post("/login/")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_email(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/")
async def list_users(token: str = Depends(oauth2_scheme)):
    user = get_user_from_token(token)
    if not user:
        raise HTTPException(status_code=403, detail="Not authorized")
    users = get_all_users()
    return users

@app.post("/logout/")
async def logout():
    return {"msg": "Logged out successfully"}
