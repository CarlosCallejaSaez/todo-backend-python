from model import Todo
import motor.motor_asyncio

from motor.motor_asyncio import AsyncIOMotorClient

from dotenv import load_dotenv
import os


load_dotenv()


mongo_uri = os.getenv("MONGO_URI")


if not mongo_uri:
    raise ValueError("La variable de entorno MONGO_URI no está configurada.")

client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
db = client.pythonTODO
collection = db.todo   


async def get_one_todo(title):
    document = await collection.find_one({"title": title})
    return document


async def get_all_todos():
  todos = []
  cursor = collection.find({})  
  async for document in cursor:
    todos.append(Todo(**document))
  
  return todos

async def create_todo(todo):
  document = todo
  result = await collection.insert_one(document)
  return document

async def update_todo(title, desc):
  await collection.update_one(
    {"title":title},
    {'$set'  : {"description": desc}}
  )
  document = await collection.find_one({"title": title})
  return document


async  def remove_todo(title):
  await collection.delete_one({"title": title})
  return True