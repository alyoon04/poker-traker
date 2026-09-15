from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/first")
def read_first():
    return {"message": "This is the first endpoint."}