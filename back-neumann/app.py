from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"welcome": "Welcome to Von Neumann Simulator"}