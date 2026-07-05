from typing import Dict

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

items: Dict[int, dict] = {
    1: {"id": 1, "name": "Laptop"},
    2: {"id": 2, "name": "Phone"},
}
next_id = 3


class ItemCreate(BaseModel):
    name: str


class ItemUpdate(BaseModel):
    name: str


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Item Manager</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            input, button { padding: 8px; margin: 5px 0; }
            #items { margin-top: 20px; }
            .item { border-bottom: 1px solid #ccc; padding: 8px 0; }
        </style>
    </head>
    <body>
        <h1>Item Manager</h1>

        <h3>Add Item</h3>
        <input id="newName" placeholder="Item name" />
        <button onclick="addItem()">Add</button>

        <h3>Update Item</h3>
        <input id="updateId" placeholder="Item ID" />
        <input id="updateName" placeholder="New item name" />
        <button onclick="updateItem()">Update</button>

        <div id="items"></div>

        <script>
            async function loadItems() {
                const response = await fetch('/items');
                const data = await response.json();
                const container = document.getElementById('items');
                container.innerHTML = '';

                data.items.forEach(item => {
                    const div = document.createElement('div');
                    div.className = 'item';
                    div.innerHTML = `<strong>ID:</strong> ${item.id} - <strong>Name:</strong> ${item.name}`;
                    container.appendChild(div);
                });
            }

            async function addItem() {
                const name = document.getElementById('newName').value;
                if (!name) return alert('Please enter a name');

                const response = await fetch('/items', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name })
                });

                const data = await response.json();
                alert('Added: ' + JSON.stringify(data));
                document.getElementById('newName').value = '';
                loadItems();
            }

            async function updateItem() {
                const id = document.getElementById('updateId').value;
                const name = document.getElementById('updateName').value;
                if (!id || !name) return alert('Please enter item id and new name');

                const response = await fetch(`/items/${id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name })
                });

                const data = await response.json();
                alert('Updated: ' + JSON.stringify(data));
                document.getElementById('updateId').value = '';
                document.getElementById('updateName').value = '';
                loadItems();
            }

            loadItems();
        </script>
    </body>
    </html>
    """


@app.get("/items")
def get_items():
    return {"items": list(items.values())}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.post("/items")
def create_item(item: ItemCreate):
    global next_id
    new_item = {"id": next_id, "name": item.name}
    items[next_id] = new_item
    next_id += 1
    return new_item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemUpdate):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id]["name"] = item.name
    return items[item_id]
