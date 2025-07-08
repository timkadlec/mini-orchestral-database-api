# Mini Orchestral Database API 🎻

This is a minimal Flask-based REST API for managing orchestral projects and their instrumentation.  
The purpose of this repository is to demonstrate the backend architecture and API logic I commonly use in larger applications.

> ⚠️ This project is a simplified version of a real-world orchestral management system I developed (`cnso_app`).  
> It does **not** include full orchestration planning, player assignments, permissions, or a frontend.

---

## Features

- CRUD for Instruments and Projects
- Ability to assign instruments to projects
- SQLite database with SQLAlchemy
- Modular structure using Flask Blueprints
- RESTful API design

---

## Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/timkadlec/mini-orchestral-database-api.git
cd mini-orchestral-database-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python run.py
```

> The app will be available at `http://127.0.0.1:5000`

---

## Example API Usage

### Get instruments

```http
GET /api/instruments
```

### Add an instrument

```http
POST /api/instruments
Content-Type: application/json

{
  "name": "Trumpet",
  "abbreviation": "Tpt"
}
```

### Add a project

```http
POST /api/projects
Content-Type: application/json

{
  "title": "Mahler 5"
}
```

### Assign instrument to project

```http
POST /api/project-instrumentation
Content-Type: application/json

{
  "project_id": 1,
  "instrument_id": 2,
  "count": 4
}
```

---

## Technologies

- Python 3.13
- Flask
- SQLAlchemy
- SQLite

---

## Author

Tim Kadlec  
PhD student, flutist, and backend developer.
