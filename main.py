from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

app = FastAPI()

@app.get("/health")
def read_health():
    return {"status": "ok"}

@app.post("/login")
async def login(request: LoginRequest):
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3003)
