from fastapi import FastAPI

# from app.sections import sections
from app.patients import patients
from app.sequence import sequence

# Initialize app
app = FastAPI()

app.include_router(patients.router)
# app.include_router(sections.router)
app.include_router(sequence.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}