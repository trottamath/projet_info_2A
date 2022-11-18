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


# Lancement de l'application sur le le port 8XXX avec XXX les 3 derniers numéros de votre id
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8058)


    class Todo(BaseModel):
    id : int
    content : str
    todos = {1 : Todo(1, "Step 1 : Learn python"),
        , 2 : Todo(2,"Step 2 : Work on the IT project")
        , 3 : Todo(3,"Step 3 : ???")
        , 4 : Todo(4,"Step 4 : Profit")}
