from fastapi import FastAPI
from backend.routes.user import routes

app = FastAPI()
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Hello from your FastAPI app!"}
