from fastapi import FastAPI
from routes.user import user_router

app = FastAPI()
app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "Hello from your FastAPI app!"}
