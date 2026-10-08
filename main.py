from fastapi import FastAPI
app=FastAPI()

@app.get("/")

def test():
    return {"message": "Hello, World . Learnng API with FastAPI is fun!"} 