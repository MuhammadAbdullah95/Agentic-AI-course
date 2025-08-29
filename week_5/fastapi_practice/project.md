# 📘 Mini Project: Student Management API

## 🎯 Goal

Build a FastAPI backend to manage students in a class. Students can **be added, updated, deleted, and retrieved**. Users should also be able to **filter/search** students using query parameters.

---

## 🛠 Features to Implement

1. **CRUD Operations**

   * `POST /students/` → Add a new student.
   * `GET /students/` → Get all students.
   * `GET /students/{student_id}` → Get a single student (Path Param).
   * `PUT /students/{student_id}` → Update a student’s details.
   * `DELETE /students/{student_id}` → Remove a student.

2. **Request & Response Models**

   * `StudentCreate` (Request model for adding/updating).
   * `Student` (Response model with `id` included).

3. **Query Parameters**

   * `GET /students/?age=20` → Filter by age.
   * `GET /students/?name=Ali` → Search by name.
   * `GET /students/?age=20&name=Ali` → Combine filters.

---

## 📂 Example Models

```python
from pydantic import BaseModel
from typing import List, Optional

# Request model
class StudentCreate(BaseModel):
    name: str
    age: int
    grade: str

# Response model
class Student(StudentCreate):
    id: int
```

---

## 🏗 Expected Flow

* Add new students with `POST`.
* Get all students or filter them with **query params**.
* Fetch a specific student using **path params**.
* Update or delete a student by ID.

---

## 🌟 Example Tasks for Students

1. Implement all endpoints using an in-memory list (no database).
2. Ensure validation works (e.g., `age` must be positive).
3. Add filtering with query params (case-insensitive search for names).
4. Return proper error messages with `HTTPException`.

---

## 🔍 Sample Input/Output

### **POST /students/**

Request:

```json
{
  "name": "Ali",
  "age": 21,
  "grade": "A"
}
```

Response:

```json
{
  "id": 1,
  "name": "Ali",
  "age": 21,
  "grade": "A"
}
```

### **GET /students/?age=21**

Response:

```json
[
  {
    "id": 1,
    "name": "Ali",
    "age": 21,
    "grade": "A"
  }
]
```

---

## ✅ Learning Outcomes

This project helps students practice:

* CRUD operations
* Request Body + Response Models
* Path & Query Params
* Error Handling

It is simple enough for beginners but covers all the topics learned so far.
