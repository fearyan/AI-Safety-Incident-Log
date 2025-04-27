# HumanChain AI Safety Incident Log API

A simple RESTful API service to log and manage hypothetical AI safety incidents. Includes endpoints to create, view, and delete incidents, with data stored in a database. Built for HumanChain’s AI Safety Incident Log assignment.

## Tech Stack

- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite (default, easy to switch to PostgreSQL/MySQL)

## Setup Instructions

1. **Clone the repo**  
   `git clone https://github.com/fearyan/AI-Safety-Incident-Log.git && cd incident_log_api`

2. **Install dependencies**  
   `pip install -r requirements.txt`

3. **Initialize the database with sample data**  
   `python db_init.py`

4. **Run the server**  
   `python app.py`

## API Endpoints

### 1. Get all incidents

- **GET** `/incidents`
- **Response:**  
  `200 OK`
```json
[
  {
    "id": 1,
    "title": "...",
    "description": "...",
    "severity": "...",
    "reported_at": "..."
  }
]
```

### 2. Create a new incident

- **POST** `/incidents`
- **Request Body:**
```json
{
  "title": "New Incident Title",
  "description": "Detailed description here.",
  "severity": "Medium"
}
```
- **Response:**  
  `201 Created`
```json
{
  "id": 3,
  "title": "New Incident Title",
  "description": "Detailed description here.",
  "severity": "Medium",
  "reported_at": "2025-04-02T18:00:00Z"
}
```

### 3. Get incident by ID

- **GET** `/incidents/{id}`

### 4. Delete incident by ID

- **DELETE** `/incidents/{id}`

## Design Notes

- Uses Flask and SQLAlchemy for simplicity and readability.
- SQLite for easy local setup (can switch to PostgreSQL/MySQL).
- Basic validation and error handling included.

---

## Example `curl` Commands

**Get all incidents:**
```sh
curl -X GET http://127.0.0.1:5000/incidents
```

**Create a new incident:**
```sh
curl -X POST http://127.0.0.1:5000/incidents \
  -H "Content-Type: application/json" \
  -d '{"title": "Test", "description": "Test desc", "severity": "Low"}'
```

**Get incident by ID:**
```sh
curl -X GET http://127.0.0.1:5000/incidents/1
```

**Delete incident by ID:**
```sh
curl -X DELETE http://127.0.0.1:5000/incidents/1
```
```

---

### (Optional) `.env`

If you want to use a different database, create a `.env` file:
```
DATABASE_URL=sqlite:///incidents.db
