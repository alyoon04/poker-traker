from fastapi import FastAPI

from pydantic import BaseModel

class Session(BaseModel): #basemodel is a  class from pydantic that knows how to parse incoming json. Session is a child inheriting form basemodel
   date: str # no fallback values, so required fields that dont have a fallback value and give error instead
   location: str
   stakes: str
   buy_in: float
   cash_out: float

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.get("/sessions/{session_id}")
def read_session(session_id: int):
    return {"session_id": session_id}

@app.get("/sessions")
def read_sessions(limit: int = 10):
    return {"limit": limit}

@app.post("/sessions")
def sessions(session: Session):
    return {"session": session}