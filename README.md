# AgentAPI (FastAPI)

A minimal FastAPI service with a couple of example endpoints.

## Quickstart (Windows PowerShell)

```powershell
# 1) Create and activate a virtual environment (Python 3.10+ recommended)
python -m venv .venv
. .venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the server (reload for dev)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Then open `http://localhost:8000/docs` for the interactive Swagger UI.

## Endpoints

- `GET /` — root metadata
- `GET /health` — simple health check
- `POST /echo` — echoes a JSON `{ "message": "..." }`

## Project layout

```
app/
  __init__.py
  main.py
requirements.txt
README.md
.gitignore
```

## Notes
- Prefer running inside a virtual environment.
- Use `--reload` only for development.

