from fastapi import FastAPI
from .routers import patients

# Initialize app
app = FastAPI()

app.include_router(patients.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}