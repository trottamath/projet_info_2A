from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Lancement de l'application 
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80) 