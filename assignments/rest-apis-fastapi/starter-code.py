from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# TODO: Define a Pydantic model for your data structure
# Example: class Todo(BaseModel): ...

# TODO: Create an in-memory data store (list or dictionary)
# Example: todos: List[Todo] = []

# TODO: Implement GET endpoint to retrieve all items
# Route: GET /

# TODO: Implement POST endpoint to create a new item
# Route: POST /

# TODO: Implement GET endpoint to retrieve a single item by ID
# Route: GET /{item_id}

# TODO: Implement PUT endpoint to update an item
# Route: PUT /{item_id}

# TODO: Implement DELETE endpoint to remove an item
# Route: DELETE /{item_id}

# TODO: Add query parameter support for filtering
# Example: GET /?status=completed

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
