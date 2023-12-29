from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo



app = FastAPI()


from database import (
  get_one_todo,
  get_all_todos,
  create_todo,
  update_todo,
  remove_todo
)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return {"Developed with ♥": "by Carlos Calleja Saez"}


@app.get("/api/todo")
async def get_todo():
    response = await get_all_todos()
    return response


@app.get("/api/todo/{title}",response_model=Todo)
async def get_todo(title):
    response = await get_one_todo(title)
    if response:
      return response
    raise HTTPException(404, f"No todo found with title: {title}")


@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Bad Request")


@app.put("/api/todo/{title}", response_model=Todo)
async def put_todo(todo: Todo):
    newTitle = todo.title
    newDesc = todo.description
    response = await update_todo(newTitle, newDesc)
    if response:
      return response
    raise HTTPException(404, "No todo found with title: {title}")


@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response =  await remove_todo(title)
    if response:
      return "Todo deleted successfully"
    raise HTTPException(404, f"No todo found with title: {title}")