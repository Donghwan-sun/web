import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from app.router import user, auth

app = FastAPI()

origins =[
    settings.CLIENT_ORIGIN
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=["Auth"], prefix="/api/auth")
app.include_router(user.router, tags=["Users"], prefix="/api/users")

@app.get("/apis/health")
def health():
    return {"message": "health"}

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8081, reload=True)
