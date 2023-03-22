from fastapi import FastAPI

from .sections import sections
from .patients import patients
from .sequence import sequence

# Initialize app
app = FastAPI()

app.include_router(patients.router)
app.include_router(sections.router)
app.include_router(sequence.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}