# 🚀 Mini Project: Blog & File Upload API (Beginner Level)

## Objective

Build a simple FastAPI application where students can:

-   Create, read, update, and delete blog posts.
-   Upload and download files.

## Core Features

### Blog API (CRUD)

-   `POST /blogs/` → Create a blog post (title, content).
-   `GET /blogs/` → List all blogs.
-   `GET /blogs/{id}` → Get a single blog by ID.
-   `PUT /blogs/{id}` → Update a blog.
-   `DELETE /blogs/{id}` → Delete a blog.

### File Upload API

-   `POST /upload/` → Upload a file (save locally in `uploads/` folder).
-   `GET /files/{filename}` → Download a file.

## Learning Goals

-   Understand how FastAPI handles requests and responses.
-   Work with request body, query parameters, and path parameters.
-   Learn file handling in FastAPI.
-   Practice project structuring (routers, models, etc.).

------------------------------------------------------------------------

👉 Note:\
**"This is your beginner-level mini project. Build the Blog & File
Upload API step by step, and get your hands dirty by extending it with
new features, like adding an author field for blogs or validating file
types on upload."**
