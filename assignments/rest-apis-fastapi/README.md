# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework to understand HTTP methods, request/response handling, and API endpoint design. You'll create a functioning API with CRUD operations and learn how modern web services handle client requests.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description

Set up a FastAPI application with GET and POST endpoints. Define data models using Pydantic and implement endpoints to create and retrieve items from an in-memory data store.

#### Requirements

Completed program should:

- Initialize a FastAPI application with proper imports and app instance
- Define a Pydantic model for items (e.g., Todo, Product, Student)
- Implement a GET endpoint to retrieve all items
- Implement a POST endpoint to create new items with validation
- Return appropriate JSON responses with status codes

---

### 🛠️ Handle Path and Query Parameters

#### Description

Extend the API with dynamic endpoints using path parameters and query parameters. Implement individual item retrieval and filtering capabilities.

#### Requirements

Completed program should:

- Create a GET endpoint with a path parameter to retrieve a single item by ID
- Implement query parameters to filter or search items (e.g., by name, status)
- Return 404 errors when items are not found
- Accept and validate optional query parameters

---

### 🛠️ Implement Full CRUD Operations

#### Description

Complete the API by adding update (PUT/PATCH) and delete (DELETE) operations. Ensure proper error handling and data validation throughout.

#### Requirements

Completed program should:

- Implement PUT endpoint to update existing items completely
- Implement DELETE endpoint to remove items by ID
- Validate that required fields are present before updating
- Return appropriate HTTP status codes for all operations (200, 201, 204, 404)
- Include proper error messages for validation failures
