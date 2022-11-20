"""module fastapi.py
version 1.0
date 18/11/2022
auteure : Justine Farnarier
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Lancement de l'application 
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80) 