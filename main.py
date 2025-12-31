from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

class LoginRequest(BaseModel):
    username: str
    password: str

class AskRequest(BaseModel):
    question: str


VALID_USERS = [
    {"username": "matt", "password": "password"},
    {"username": "kate", "password": "password"},
    {"username": "anne", "password": "password"},
]

def is_valid_user(user_credentials: LoginRequest) -> bool:
    for user in VALID_USERS:
        if user["username"] == user_credentials.username and user["password"] == user_credentials.password:
            return True
    return False

app = FastAPI()

use_cors = os.getenv('USE_CORS', 'False').lower() == 'true'
print(f"CORS Enabled: {use_cors}")

if use_cors:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/health")
def read_health():
    return {"status": "ok"}

@app.post("/api/ask")
async def ask(request: AskRequest):
    return {"status": "ok"}

@app.post("/api/login")
async def login(request: LoginRequest):
    if not is_valid_user(request):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return {"status": "ok"}

@app.post("/api/logout")
async def logout():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3003)
