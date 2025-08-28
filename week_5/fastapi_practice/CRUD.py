import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utitls import read_json_file, write_json_file
from schema import Item, SignIn

app = FastAPI()

DATA_FILE = "items.json" #Global Variable

# ------------------------
# Dummy User Data
# ------------------------
user_data = {"username": "admin", "password": "secret"}


# ------------------------
# Routes
# ------------------------
@app.get("/")
async def hello():
    return {"message": "Hello, World!"}


@app.get("/signin/")
def signin(user: SignIn):
    if user.username == user_data["username"] and user.password == user_data["password"]:
        return {"message": "Sign-in successful"}
    return {"error": "Invalid username or password"}


# ------------------------
# CRUD Endpoints
# ------------------------




# READ ALL
@app.get("/items/")
def get_items():
    return read_json_file(DATA_FILE)


# READ ONE
@app.get("/items/{item_id}") #path parameter
def get_item(item_id: str):
    items = read_json_file(DATA_FILE)
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


# CREATE
@app.post("/items/")
def create_item(item: Item):
    items = read_json_file(DATA_FILE)
    # Check if ID already exists
    if any(existing_item["id"] == item.id for existing_item in items):
        raise HTTPException(status_code=400, detail="Item ID already exists")
    items.append(item.dict())
    write_json_file(DATA_FILE, items)
    return {"message": "Item created successfully", "item": item}


# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: str, updated_item: Item):
    items = read_json_file(DATA_FILE)
    for i, item in enumerate(items):
        if item["id"] == item_id:
            items[i] = updated_item.dict()
            write_json_file(DATA_FILE, items)
            return {"message": "Item updated successfully", "item": updated_item}
    raise HTTPException(status_code=404, detail="Item not found")


# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    items = read_json_file(DATA_FILE)
    for i, item in enumerate(items):
        if item["id"] == item_id:
            deleted_item = items.pop(i)
            write_json_file(DATA_FILE, items)
            return {"message": "Item deleted successfully", "item": deleted_item}
    raise HTTPException(status_code=404, detail="Item not found")
