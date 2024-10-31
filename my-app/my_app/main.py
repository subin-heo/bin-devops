from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "HI subin"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
