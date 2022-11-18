# Import classique
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Définition du endpoint get /todo
@app.get("/")
async def get_all_todo():
    return todos.values()


# Définition du endpoint get /todo/{id_doto}
@app.get("/todo/{id_toto}")
async def get_todo_by_id(id_toto : int = Path(..., description = "The id of the todo you want to get")):
    if todos.get[id_toto] :
        return todos.get[id_toto]
    else :
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)


# Définition du endpoint post /todo
@app.post("/todo", todo, status_code=201)
async def post_todo(todo:Todo):
    if not todos.get(todo.id):
        return JSONResponse(status_code=status.HTTP_409_CONFLICT)
    else :
     todos[todo.id] = todo
        return todo

# Lancement de l'application sur le port 8XXX avec id personnel : 
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8058)



# Import classique
from fastapi import FastAPI
# On instancie le webservice
app = FastAPI()
# Création d'un enpoint qui répond à la méthode GET à l'adresse "/" qui va
retourne le message "Hello World"
@app.get("/")
async def root():
    return {"message": "Hello World"}
# Lancement de l'application sur le le port 80
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.1.0", port=8058)

