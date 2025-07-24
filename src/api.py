
from fastapi import FastAPI
from pydantic import BaseModel


from src.generator import generate_answer

app = FastAPI()

class QueryReq(BaseModel):
    query: str

@app.post("/ask")
def ask(req: QueryReq):
    try:
        ans = generate_answer(req.query)
        return {"answer": ans}
    except Exception as e:
        return {"error": str(e)}



# uvicorn src.api:app --reload
